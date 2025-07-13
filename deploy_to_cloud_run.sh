#!/bin/bash

# This script automates the build and deployment of the Adaptive Identity Guardian
# web application to Google Cloud Run.
# It assumes you have gcloud CLI installed and configured, and Docker installed.

# --- Configuration Parameters ---
# Replace these values with your specific project details
PROJECT_ID="Cyberark_research" # Your Google Cloud Project ID
REGION="us-central1"             # The Google Cloud region for your Cloud Run service (e.g., us-central1, europe-west1)
SERVICE_NAME="adaptive-identity-guardian" # The name of your Cloud Run service
ALLOW_UNAUTHENTICATED="--allow-unauthenticated" # Set to "--no-allow-unauthenticated" for restricted access

# --- Script Logic ---

echo "--- Starting Cloud Run Deployment ---"
echo "Project ID: $PROJECT_ID"
echo "Region: $REGION"
echo "Service Name: $SERVICE_NAME"

# 1. Get the current commit SHA to tag the Docker image
# This ensures unique image versions for each deployment
COMMIT_SHA=$(git rev-parse HEAD)
if [ -z "$COMMIT_SHA" ]; then
  echo "Error: Could not determine Git commit SHA. Please run this script in a Git repository."
  exit 1
fi
echo "Using Git Commit SHA: $COMMIT_SHA"

# 2. Build the Docker image
# The Dockerfile and application code (index.html, main.py, requirements.txt)
# are expected to be in the current directory.
echo "Building Docker image: gcr.io/$PROJECT_ID/$SERVICE_NAME:$COMMIT_SHA"
docker build -t gcr.io/$PROJECT_ID/$SERVICE_NAME:$COMMIT_SHA .

# Check if docker build was successful
if [ $? -ne 0 ]; then
  echo "Error: Docker image build failed."
  exit 1
fi
echo "Docker image built successfully."

# 3. Push the Docker image to Google Container Registry (GCR)
echo "Pushing Docker image to GCR..."
docker push gcr.io/$PROJECT_ID/$SERVICE_NAME:$COMMIT_SHA

# Check if docker push was successful
if [ $? -ne 0 ]; then
  echo "Error: Docker image push failed."
  exit 1
fi
echo "Docker image pushed to GCR."

# 4. Deploy the service to Cloud Run
# This command creates or updates the Cloud Run service with the new image.
echo "Deploying $SERVICE_NAME to Cloud Run in region $REGION..."
gcloud run deploy "$SERVICE_NAME" \
  --image "gcr.io/$PROJECT_ID/$SERVICE_NAME:$COMMIT_SHA" \
  --region "$REGION" \
  --platform "managed" \
  $ALLOW_UNAUTHENTICATED \
  --project "$PROJECT_ID" # Explicitly specify project for clarity

# Check if gcloud run deploy was successful
if [ $? -ne 0 ]; then
  echo "Error: Cloud Run deployment failed."
  exit 1
fi

echo "--- Deployment Complete! ---"
echo "Your service '$SERVICE_NAME' should now be accessible."
echo "You can find its URL in the Google Cloud Console or by running:"
echo "gcloud run services describe $SERVICE_NAME --region $REGION --project $PROJECT_ID --format 'value(status.url)'"
