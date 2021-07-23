import base64
import main
import mock
import time

svc_update_message = """
{
  "insertId": "xxxxxxxxxx",
  "logName": "projects/xxxxxxxxxx/logs/cloudaudit.googleapis.com%2Fsystem_event",
  "protoPayload": {
    "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
    "resourceName": "namespaces/xxxxxxxxxx/services/hello",
    "response": {
      "@type": "type.googleapis.com/google.cloud.run.v1.Service",
      "apiVersion": "serving.knative.dev/v1",
      "kind": "Service",
      "metadata": {
        "annotations": {
          "client.knative.dev/user-image": "gcr.io/google-samples/hello-app:1.0",
          "run.googleapis.com/client-name": "cloud-console",
          "run.googleapis.com/ingress": "all",
          "run.googleapis.com/ingress-status": "all",
          "serving.knative.dev/creator": "email@example.com",
          "serving.knative.dev/lastModifier": "email@example.com"
        },
        "creationTimestamp": "2021-07-22T20:41:06.007828Z",
        "generation": 4,
        "labels": {
          "cloud.googleapis.com/location": "us-central1"
        },
        "name": "hello",
        "namespace": "000000000000",
        "resourceVersion": "AAXHvgA/qd0",
        "selfLink": "/apis/serving.knative.dev/v1/namespaces/00000000000/services/hello",
        "uid": "24fbc482-67a1-4951-8407-a69cba95fb70"
      },
      "spec": {
        "template": {
          "metadata": {
            "annotations": {
              "autoscaling.knative.dev/maxScale": "100",
              "run.googleapis.com/client-name": "cloud-console",
              "run.googleapis.com/sandbox": "gvisor"
            },
            "name": "hello-00004-vij"
          },
          "spec": {
            "containerConcurrency": 80,
            "containers": [
              {
                "image": "gcr.io/google-samples/hello-app:1.0",
                "ports": [
                  {
                    "containerPort": 8080
                  }
                ],
                "resources": {
                  "limits": {
                    "cpu": "1000m",
                    "memory": "512Mi"
                  }
                }
              }
            ],
            "serviceAccountName": "00000000000-compute@developer.gserviceaccount.com",
            "timeoutSeconds": 300
          }
        },
        "traffic": [
          {
            "latestRevision": true,
            "percent": 100
          }
        ]
      },
      "status": {
        "address": {
          "url": "https://hello-xxxxxxxxxx-uc.a.run.app"
        },
        "conditions": [
          {
            "lastTransitionTime": "2021-07-22T22:42:25.439197Z",
            "status": "True",
            "type": "Ready"
          },
          {
            "lastTransitionTime": "2021-07-22T22:42:19.774378Z",
            "status": "True",
            "type": "ConfigurationsReady"
          },
          {
            "lastTransitionTime": "2021-07-22T22:42:25.439197Z",
            "status": "True",
            "type": "RoutesReady"
          }
        ],
        "latestCreatedRevisionName": "hello-00004-vij",
        "latestReadyRevisionName": "hello-00004-vij",
        "observedGeneration": 4,
        "traffic": [
          {
            "latestRevision": true,
            "percent": 100,
            "revisionName": "hello-00004-vij"
          }
        ],
        "url": "https://hello-xxxxxxxxxx-uc.a.run.app"
      }
    },
    "serviceName": "run.googleapis.com",
    "status": {
      "message": "Ready condition status changed to True for Service hello."
    }
  },
  "receiveTimestamp": "2021-07-22T22:42:26.335728956Z",
  "resource": {
    "labels": {
      "configuration_name": "",
      "location": "us-central1",
      "project_id": "xxxxxxxxxx",
      "revision_name": "",
      "service_name": "hello"
    },
    "type": "cloud_run_revision"
  },
  "severity": "INFO",
  "timestamp": "2021-07-22T22:42:25.423707Z"
}
"""
svc_delete_message = """
{
  "insertId": "xxxxxxxxxx",
  "logName": "projects/xxxxxxxxxx/logs/cloudaudit.googleapis.com%2Fsystem_event",
  "protoPayload": {
    "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
    "resourceName": "namespaces/xxxxxxxxxx/services/hello",
    "response": {
      "@type": "type.googleapis.com/google.cloud.run.v1.Service",
      "apiVersion": "serving.knative.dev/v1",
      "kind": "Service",
      "metadata": {
        "annotations": {
          "client.knative.dev/user-image": "gcr.io/google-samples/hello-app:1.0",
          "run.googleapis.com/client-name": "cloud-console",
          "run.googleapis.com/ingress": "all",
          "run.googleapis.com/ingress-status": "all",
          "serving.knative.dev/creator": "email@example.com",
          "serving.knative.dev/lastModifier": "email@example.com"
        },
        "creationTimestamp": "2021-07-07T17:28:39.588015Z",
        "deletionTimestamp": "2021-07-22T22:54:55.701873Z",
        "generation": 5,
        "labels": {
          "cloud.googleapis.com/location": "us-central1"
        },
        "name": "hello",
        "namespace": "000000000000",
        "resourceVersion": "AAXHvi0uXtA",
        "selfLink": "/apis/serving.knative.dev/v1/namespaces/000000000000/services/hello",
        "uid": "b784f5dc-cbf6-4269-b30d-46b703781878"
      },
      "spec": {
        "template": {
          "metadata": {
            "annotations": {
              "autoscaling.knative.dev/maxScale": "100",
              "run.googleapis.com/client-name": "cloud-console",
              "run.googleapis.com/sandbox": "gvisor"
            },
            "name": "hello-00004-xat"
          },
          "spec": {
            "containerConcurrency": 1,
            "containers": [
              {
                "image": "gcr.io/google-samples/hello-app:1.0",
                "ports": [
                  {
                    "containerPort": 8080
                  }
                ],
                "resources": {
                  "limits": {
                    "cpu": "1000m",
                    "memory": "256Mi"
                  }
                }
              }
            ],
            "serviceAccountName": "000000000000-compute@developer.gserviceaccount.com",
            "timeoutSeconds": 300
          }
        },
        "traffic": [
          {
            "latestRevision": true,
            "percent": 100
          }
        ]
      },
      "status": {
        "address": {
          "url": "https://hello-xxxxxxxxxx-uk.a.run.app"
        },
        "conditions": [
          {
            "lastTransitionTime": "2021-07-22T22:54:59.280592Z",
            "message": "Deletion in progress.",
            "status": "True",
            "type": "Ready"
          },
          {
            "lastTransitionTime": "2021-07-22T20:47:19.295269Z",
            "status": "True",
            "type": "ConfigurationsReady"
          },
          {
            "lastTransitionTime": "2021-07-22T20:47:24.794330Z",
            "status": "True",
            "type": "RoutesReady"
          }
        ],
        "latestCreatedRevisionName": "hello-00004-xat",
        "latestReadyRevisionName": "hello-00004-xat",
        "observedGeneration": 5,
        "traffic": [
          {
            "latestRevision": true,
            "percent": 100,
            "revisionName": "hello-00004-xat"
          }
        ],
        "url": "https://hello-xxxxxxxxxx-uk.a.run.app"
      }
    },
    "serviceName": "run.googleapis.com",
    "status": {
      "message": "Ready condition status changed to True for Service hello with message: Deletion in progress."
    }
  },
  "receiveTimestamp": "2021-07-22T22:55:00.042388327Z",
  "resource": {
    "labels": {
      "configuration_name": "",
      "location": "us-central1",
      "project_id": "xxxxxxxxxx",
      "revision_name": "",
      "service_name": "hello"
    },
    "type": "cloud_run_revision"
  },
  "severity": "INFO",
  "timestamp": "2021-07-22T22:54:59.257588Z"
}
"""
add_record_audit_event = {
    'data': base64.b64encode(svc_update_message.encode())}
del_record_audit_event = {
    'data': base64.b64encode(svc_delete_message.encode())}

mock_context = mock.Mock()
mock_context.event_id = '000000000000'
mock_context.timestamp = '2021-07-22T22:55:00.523Z'
mock_context.resource = {
    'name': 'projects/xxxxxxxxxx/topics/xxxxxxxxxx',
    'service': 'pubsub.googleapis.com',
    'type': 'type.googleapis.com/google.pubsub.v1.PubsubMessage',
}


def test():
    # test adding new record
    main.audit_event(add_record_audit_event, mock_context)
    # test replacing existing record
    main.audit_event(add_record_audit_event, mock_context)
    # test deleting existing record
    main.audit_event(del_record_audit_event, mock_context)
    # test deleting non-existing record
    main.audit_event(del_record_audit_event, mock_context)


test()
