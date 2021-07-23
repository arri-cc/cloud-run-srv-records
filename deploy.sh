#!/bin/sh
gcloud functions deploy cloud-run-srv-records \
    --entry-point audit_event \
    --trigger-topic cloud_run_rev_audit \
    --runtime python39 \
    --region us-east4 \
    --service-account cloudrun-srv-records@arri-primary.iam.gserviceaccount.com