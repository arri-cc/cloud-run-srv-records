from google.cloud import dns
import base64
import json
import sys
import time
from types import SimpleNamespace

from google.cloud.dns.zone import ManagedZone


def audit_event(event, context):
    project = 'arri-ti-demo'
    dns_zone_name = 'svc.local'
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

    svc_name = event_data.protoPayload.request.service.metadata.name
    svc_url = event_data.protoPayload.request.service.status.url
    svc_port = 443  # always the same for now

    print(f'name: {svc_name} url: {svc_url} port: {svc_port}')
    update_dns_record(dns_zone, svc_name, svc_url, svc_port, True)


def update_dns_record(zone: ManagedZone, dns_record_name, url, port, add=True, ):
    changes = zone.changes()

    dns_record_type = "SRV"
    #ttl in seconds
    dns_record_ttl = 600
    # a RecordSet supports an array of answers as a list of strings
    # create a new RecordSet with SRV type. The SRV Data is formatted
    # <priority> <weight> <port> <url>
    # e.g.: 0 1 443 example.com
    dns_record_data = [f'0 1 {port} {url}']

    dns_record = zone.resource_record_set(
        dns_record_name, dns_record_type, dns_record_ttl, dns_record_data)

    if add:
        print(
            f'adding dns record {dns_record_name} {dns_record_ttl} {dns_record_data}')
        changes.add_record_set(dns_record)
    else:
        print(
            f'deleting dns record {dns_record_name} {dns_record_ttl} {dns_record_data}')
        changes.delete_record_set(dns_record)

    # create the changes
    changes.create()

    # wait for changes to complete
    while changes.status() != 'done':
        time.sleep(5)
        changes.reload()
