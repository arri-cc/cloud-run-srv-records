from google.cloud import dns
import base64
import json
import os
import sys
import time
from types import SimpleNamespace
from urllib.parse import urlparse
from google.cloud.dns.resource_record_set import ResourceRecordSet

from google.cloud.dns.zone import ManagedZone


def audit_event(event, context):
    project = os.getenv('PROJECT')
    dns_zone_name = 'svc-local'
    dns_client = dns.Client(project=project)
    dns_zone = dns_client.zone(dns_zone_name)

    if not dns_zone.exists():
        print(
            f'Unable to handle audit event, zone {dns_zone_name} does not exist.  eventid: {context.event_id} time: {context.timestamp} resource: {context.resource["name"]}', file=sys.stderr)
        return

    print(
        f'Processing audit event with eventid: {context.event_id} time: {context.timestamp} resource: {context.resource["name"]}')

    if 'data' in event:
        data = base64.b64decode(event['data']).decode('utf-8')
        event_data = json.loads(
            data, object_hook=lambda d: SimpleNamespace(**d))
    else:
        print(
            f'no data available in event: {context.event_id}', file=sys.stderr)
        return

    svc_name = f'_run._tcp.{event_data.protoPayload.response.metadata.name}.svc.local.'
    svc_host = urlparse(
        event_data.protoPayload.response.status.address.url).hostname
    svc_port = 443  # always the same for now
    add_record = 'Deletion' not in event_data.protoPayload.status.message

    print(f'name: {svc_name} host: {svc_host} port: {svc_port}')

    existing_dns_record = get_existing_dns_record(dns_zone, svc_name)

    update_dns_record(dns_zone, svc_name, svc_host,
                      svc_port, existing_dns_record, add_record)


def get_existing_dns_record(zone: ManagedZone, dns_record_name) -> ResourceRecordSet:
    existing_record_sets = list(zone.list_resource_record_sets())
    for rs in existing_record_sets:
        if rs.name == dns_record_name:
            return rs
    return None


def update_dns_record(zone: ManagedZone, dns_record_name, host, port, existing_record: ResourceRecordSet, add=True):
    changes = zone.changes()

    dns_record_type = "SRV"
    #ttl in seconds
    dns_record_ttl = 600
    # a RecordSet supports an array of answers as a list of strings
    # create a new RecordSet with SRV type. The SRV Data is formatted
    # <priority> <weight> <port> <url>
    # e.g.: 0 1 443 example.com.
    dns_record_data = [f'0 1 {port} {host}.']

    dns_record = zone.resource_record_set(
        dns_record_name, dns_record_type, dns_record_ttl, dns_record_data)

    if existing_record and add:
        print(
            f'replacing existing record {dns_record_name} {dns_record_ttl} {dns_record_data}')
        changes.delete_record_set(existing_record)
        changes.add_record_set(dns_record)

    if not existing_record and add:
        print(
            f'adding new dns record {dns_record_name} {dns_record_ttl} {dns_record_data}')
        changes.add_record_set(dns_record)

    if existing_record and not add:
        print(
            f'deleting existing dns record {dns_record_name} {dns_record_ttl} {dns_record_data}')
        changes.delete_record_set(existing_record)

    if not existing_record and not add:
        print(
            f'cannot delete dns record that does not exist {dns_record_name} {dns_record_ttl} {dns_record_data}')
        return

    # create the changes
    changes.create()

    # wait for changes to complete
    while changes.status != 'done':
        time.sleep(5)
        changes.reload()
    print(f'successfully processed changes for {dns_record_name}')
