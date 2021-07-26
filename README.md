# Cloud DNS + SRV records for Cloud Run Service Discovery

This repo provides some quick examples of how we can leverage a private Cloud DNS Managed Zone to keep SRV records up to date, allowing client applications to resolve Cloud Run services at runtime with just the name of the service.  Here are some of the benefits of this approach:

- Enables unified service discovery of Cloud Run and other services while minimizing the amount of custom code.
- By leveraging DNS we can:
  - Use the same protocol for all service discovery
  - Rely on a mature ecosystem of stable client-side dns libraries and built-in SRV resolution support
  - Avoid creating and managing a separate data repository
- *More specifically*, the use of SRV records provides a way to resolve the orginal FQDN of a Cloud Run service, which is required for authenticating requests originating from a [Service Account](https://cloud.google.com/run/docs/authenticating/service-to-service#acquire-token)



## Overview

While this repo does not provide examples for every aspect, here's an overview of the components required for this approach.

**Private Cloud DNS Managed Zone:** 

A private DNS  zone for managing records for service discovery between GCE/GKE and  Cloud Run (e.g. svc.local). We can use A or CNAME records for  services hosted on GCE/GKE and SRV records to resolve services hosted in Cloud Run. This repo is focused on the automatic management of SRV records for Cloud Run services.

**Cloud Logging Sink to PubSub:** An event stream of filtered logs from the Cloud Run audit logs to track when services are created, updated or deleted, automatically published to a Cloud PubSub topic. 

**Cloud Function with PubSub trigger:** A function that subscribes to the above logging sink's pubsub topic to extract the  service details and add/update/delete SRV records pointing to Cloud Run services in a private Cloud DNS Managed Zone.

**Serverless VPC Connector:** Allows Cloud Run services to connect to resources hosted within your  VPC as well as resolve hosts using your private Cloud DNS Managed Zone

**Add SRV record DNS resolution to workloads:** For the workloads that consume Cloud Run services, you would need to add an enhancement to  resolve the Cloud Run services by name. In the example function I've used a library called  `dnspython`. There are also implementations, like [srv_hijacker](https://github.com/rohitpaulk/srv_hijacker), that  hijack the request to replace the host:port via SRV records.



## Prequisites

Given the limited scope of the examples, here are the tasks that need to be performed prior to testing this codebase:

1. **A VPC** with a dedicated subnet for use with a Serverless VPC in your desired region.  The serverless subnet must have a `/28` CIDR.
2. **A Serverless VPC Connector:** This will be used to connect Cloud Functions and Cloud Run to your VPC to leverage the private Cloud DNS Managed Zone for DNS resolution.  You will associate this connector with the dedicated serverless subnet from step #1. Docs are [here](https://cloud.google.com/vpc/docs/configure-serverless-vpc-access).
3. **Setup a private Cloud DNS Managed Zone.**  This is a private zone for testing. This codebase **expects** a zone named `svc-local` with` svc.local` as the domain to exist.
4. **Setup a Cloud Logging Sink to PubSub:**  This is easier to do in via the Cloud Console. A file provided contains the required log filter query.  Using the Console makes it easier to setup the service account and the  with appropriate permissions.  Docs are [here](https://cloud.google.com/logging/docs/export/configure_export_v2)
   - Uses the log filter defined in  the `utils/log_query.txt`file.
   - The Cloud PubSub topic has the name `cloud-run-audit` 
5. **Setup a Service Account for managing Cloud DNS records:** For testing, setup a service account with the following attributes:
   - `cloud-run-srv-records@<project>.iam.gserviceaccount.com`, where <project> is the name of your target project
   - Grant IAM Role `DNS Administrator`  *this is just for testing. You should create a custom, least-privileged IAM role*



## Solution

Here's a brief description of what's provided.

1. **2 Cloud Functions:**

   - `src/srv_management`: This is the core function that will subscribe to your provided Cloud PubSub topic and create/update/delete SRV records based on the contents of the event.

   - `src/srv_lookup_test`: This is a test function to provide an example of using `dnspython` to perform SRV lookups using the private Cloud DNS Hosted Zone.  The provided integration test expects a record for the service yellow.  You can create this manually.  For testing with the deployed function, you can use the `name` URL parameter to specify a service name to resolve, which you can use any name that you expect to resolve. 

     ```sh
     ❯ curl "https://us-east4-some-project-name.cloudfunctions.net/cloud-run-srv-lookup-test?svc=yellow"
     host: yellow-xxxxxxxxxx-uk.a.run.app. port: 443
     ```

2. **A sample Cloud Run Service:** `utils/deploy_cloudrun.sh` Will deploy a sample app to generate the desired events that should result in new records SRV records being created.