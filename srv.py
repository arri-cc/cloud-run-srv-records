from google.cloud import dns
import base64
import json
from types import SimpleNamespace

print(f'name: {svc_name} url: {svc_url}')

def srv_pubsub(event, context):
  print(f'eventid: {context.event_id} time: {context.timestamp} resource: {context.resource["name"]')

  if 'data' in event:
    data = base64.b64decode(event['data']).decode('utf-8')
    audit_event = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
else:
    print(f'no data available in event: {context.event_id}')

svc_name = data.protoPayload.request.service.metadata.name
svc_url = data.protoPayload.request.service.status.url
svc_port = 443 #always the same for now

project_name ='arri-primary'
zone_name ='hrm.local'

client = dns.Client(project=project_name)
zone = client.zone(zone_name)

print(f'zone: {zone_name} exists? {zone.exists()}')


