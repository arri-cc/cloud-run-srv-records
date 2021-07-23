
#!bin/sh
gcloud run deploy yellow --allow-unauthenticated \
	--image gcr.io/google-samples/hello-app:1.0 \
    --cpu 1 \
    --memory 128Mi \
    --concurrency 80 \
	--min-instances 0 \
	--max-instances 1 \
    --ingress all \
	--platform managed \
    --port 443 \
    --region us-east4 \
    --vpc-connector serverless-useast4