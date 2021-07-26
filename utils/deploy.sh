
#!bin/sh
set -e

export REGION=$(gcloud config get-value compute/region)
export NAME='orange'
export VPC_CONNECTOR='serverless' #UPDATE TO YOUR

gcloud run deploy $NAME --allow-unauthenticated \
	--image gcr.io/google-samples/hello-app:1.0 \
    --cpu 1 \
    --memory 128Mi \
    --concurrency 80 \
	--min-instances 0 \
	--max-instances 1 \
    --ingress all \
	--platform managed \
    --port 443 \
    --region $REGION \
    --vpc-connector $VPC_CONNECTOR