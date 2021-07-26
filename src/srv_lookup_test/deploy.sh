#!/bin/sh
set -e
# setting values based on glcoud config
export REGION=$(gcloud config get-value compute/region)
export NAME='cloud-run-srv-lookup-test'
export VPC_CONNECTOR='serverless' #REPLACE WITH NAME OF SERVERLESS VPC CONNECTOR

gcloud functions deploy $NAME \
    --entry-point test_lookup \
    --trigger-http \
    --allow-unauthenticated \
    --ingress-settings all \
    --runtime python39 \
    --region $REGION \
    --vpc-connector $VPC_CONNECTOR
