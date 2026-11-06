# AWS Cloud Resume Challenge

## Overview

A serverless resume website independently developed and deployed using Amazon Web Services. The project combines static website hosting, a Python-powered visitor counter, infrastructure as code, and automated deployments through GitHub Actions.

The goal was to gain practical experience designing, deploying, and maintaining cloud infrastructure while building a professional engineering portfolio.

**Live Website:** https://d1vyqqqla80vif.cloudfront.net

## Architecture

**Frontend**
- Amazon S3 stores the website's static files.
- Amazon CloudFront distributes the website.
- JavaScript communicates with a REST API to retrieve and display the visitor count.

**Backend**
- Amazon API Gateway exposes the `/get-count` endpoint.
- AWS Lambda executes Python 3.11 code to process visitor requests.
- Amazon DynamoDB stores the persistent visitor count.
- Boto3 performs atomic updates to the DynamoDB record.

**Infrastructure as Code**
- AWS SAM defines the Lambda function, DynamoDB table, API Gateway integration, and associated IAM permissions.
- DynamoDB uses on-demand billing to accommodate variable traffic.

**CI/CD**
- GitHub Actions automatically deploys frontend changes when code is pushed to `main`.
- AWS OIDC federation provides temporary credentials through IAM role assumption.
- AWS CLI synchronizes frontend files to S3.
- CloudFront invalidation refreshes cached content after deployment.

## Engineering Decisions

### Serverless Architecture
Used managed AWS services to minimize infrastructure maintenance and avoid provisioning dedicated servers for a low-traffic application.

### Atomic Database Updates
Implemented DynamoDB's atomic `ADD` operation to increment the visitor count without separate read-and-write operations.

### Secure Deployment Authentication
Configured GitHub Actions to authenticate through AWS OIDC rather than storing long-lived AWS access keys.

### Automated Deployment
Created a repeatable deployment workflow to reduce manual publishing steps and maintain consistency.

## Future Improvements

- Add automated frontend and backend testing.
- Implement CloudWatch monitoring and alerting.
- Improve API request handling and throttling.
- Introduce deployment validation and rollback procedures.
- Automate backend deployment through GitHub Actions.
- Add operational documentation and availability objectives.

## Technologies

AWS · S3 · CloudFront · API Gateway · Lambda · DynamoDB · SAM · Python · Boto3 · JavaScript · IAM · OIDC · GitHub Actions
### Projects
- [Frontend](./frontend/README.md)