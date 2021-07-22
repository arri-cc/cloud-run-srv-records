

data = """
{
  "protoPayload": {
    "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
    "status": {
      "message": "Ready condition status changed to True for Service hello2."
    },
    "serviceName": "run.googleapis.com",
    "resourceName": "namespaces/arri-primary/services/hello2",
    "response": {
      "metadata": {
        "name": "hello2",
        "namespace": "583714681478",
        "selfLink": "/apis/serving.knative.dev/v1/namespaces/583714681478/services/hello2",
        "uid": "3bb526ff-065e-4b1c-a91f-414b5233c008",
        "resourceVersion": "AAXHvGQ9q5U",
        "generation": 4,
        "creationTimestamp": "2021-07-12T23:53:28.990284Z",
        "labels": {
          "cloud.googleapis.com/location": "us-east4"
        },
        "annotations": {
          "run.googleapis.com/client-name": "cloud-console",
          "serving.knative.dev/creator": "arri@doit-intl.com",
          "serving.knative.dev/lastModifier": "arri@doit-intl.com",
          "client.knative.dev/user-image": "gcr.io/google-samples/hello-app:2.0",
          "run.googleapis.com/ingress": "all",
          "run.googleapis.com/ingress-status": "all"
        }
      },
      "apiVersion": "serving.knative.dev/v1",
      "kind": "Service",
      "spec": {
        "template": {
          "metadata": {
            "name": "hello2-00004-yiz",
            "annotations": {
              "run.googleapis.com/client-name": "cloud-console",
              "autoscaling.knative.dev/maxScale": "100",
              "run.googleapis.com/sandbox": "gvisor"
            }
          },
          "spec": {
            "containerConcurrency": 80,
            "timeoutSeconds": 300,
            "serviceAccountName": "583714681478-compute@developer.gserviceaccount.com",
            "containers": [
              {
                "image": "gcr.io/google-samples/hello-app:2.0",
                "ports": [
                  {
                    "containerPort": 8080
                  }
                ],
                "resources": {
                  "limits": {
                    "cpu": "1000m",
                    "memory": "128Mi"
                  }
                }
              }
            ]
          }
        },
        "traffic": [
          {
            "percent": 100,
            "latestRevision": true
          }
        ]
      },
      "status": {
        "observedGeneration": 4,
        "conditions": [
          {
            "type": "Ready",
            "status": "True",
            "lastTransitionTime": "2021-07-22T20:47:13.095573Z"
          },
          {
            "type": "ConfigurationsReady",
            "status": "True",
            "lastTransitionTime": "2021-07-22T20:47:06.036611Z"
          },
          {
            "type": "RoutesReady",
            "status": "True",
            "lastTransitionTime": "2021-07-22T20:47:13.095573Z"
          }
        ],
        "latestReadyRevisionName": "hello2-00004-yiz",
        "latestCreatedRevisionName": "hello2-00004-yiz",
        "traffic": [
          {
            "revisionName": "hello2-00004-yiz",
            "percent": 100,
            "latestRevision": true
          }
        ],
        "url": "https://hello2-2n65kqmpcq-uk.a.run.app",
        "address": {
          "url": "https://hello2-2n65kqmpcq-uk.a.run.app"
        }
      },
      "@type": "type.googleapis.com/google.cloud.run.v1.Service"
    }
  },
  "insertId": "-oyxjcaca52",
  "resource": {
    "type": "cloud_run_revision",
    "labels": {
      "revision_name": "",
      "service_name": "hello2",
      "project_id": "arri-primary",
      "configuration_name": "",
      "location": "us-east4"
    }
  },
  "timestamp": "2021-07-22T20:47:13.081098Z",
  "severity": "INFO",
  "logName": "projects/arri-primary/logs/cloudaudit.googleapis.com%2Fsystem_event",
  "receiveTimestamp": "2021-07-22T20:47:14.503627388Z"
}
"""
