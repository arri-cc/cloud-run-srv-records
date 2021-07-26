#!/bin/sh
set -e
# setting values based on glcoud config
export PROJECT=$(gcloud config get-value project)
export REGION=$(gcloud config get-value compute/region)
export NAME='cloud-run-manage-srv-records'
export TOPIC='cloud-run-audit' # UPDATE TO CORRECT TOPIC
export SERVICE_ACCOUNT=$NAME@$PROJECT.iam.gserviceaccount.com

# deploy the function
gcloud functions deploy $NAME \
    --entry-point audit_event \
    --trigger-topic $NAME \
    --runtime python39 \
    --region $REGION \
    --service-account $SERVICE_ACCOUNT \
    --set-env-vars="PROJECT=${PROJECT}"