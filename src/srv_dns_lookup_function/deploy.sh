#!/bin/sh
gcloud functions deploy cloud-run-srv-lookup-test \
    --entry-point test_lookup \
    --trigger-http \
    --allow-unauthenticated \
    --ingress-settings all \
    --runtime python39 \
    --region us-east4 \
    --vpc-connector serverless-useast4
