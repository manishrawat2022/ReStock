#gcloud auth application-default login

export ENDPOINT_ID="3684428280305287168"
export PROJECT_ID="32393870110"
export INPUT_DATA_FILE="request.json"

curl \
-X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
https://us-central1-aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/us-central1/endpoints/${ENDPOINT_ID}:predict \
-d "@${INPUT_DATA_FILE}"