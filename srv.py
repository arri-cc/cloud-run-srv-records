from google.cloud import dns
import base64
import json
from types import SimpleNamespace



def audit_event(event, context):
  print(f'eventid: {context.event_id} time: {context.timestamp} resource: {context.resource["name"]}')

  if 'data' in event:
    data = base64.b64decode(event['data']).decode('utf-8')
    audit_event = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
  else:
    print(f'no data available in event: {context.event_id}')

  svc_name = data.protoPayload.request.service.metadata.name
  svc_url = data.protoPayload.request.service.status.url
  svc_port = 443 #always the same for now
  svc_project = 'arri-primary'
  svc_zone = 'hrm.local'
  print(f'name: {svc_name} url: {svc_url} port: {svc_port}')





def create_srv_record(project, zone_name, svc_name, svc_url, svc_port ):
  client = dns.Client(project=project)
  dns_zone = client.zone(zone_name)

  print(f'zone: {zone_name} exists? {dns_zone.exists()}')
