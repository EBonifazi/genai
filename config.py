# Imports
# Env var
import os
from ast import literal_eval
from dotenv import load_dotenv, find_dotenv

# Env variables
_ = load_dotenv(find_dotenv())

# GCP
PROJECT_ID = 'cap-hybrid-intelligence-de' 
REGION = 'us-central1'


# Vertex Search
MODEL_NAME = "gemini-1.0-pro-vision"
SEARCH_ENGINE_ID = '38f46d8a-5afc-4918-b633-d040cec5b594' #APP ID
DS_GCS_BUCKET='hig_data'
DS_INTERNAL_DOCUMENTS_FOLDER='/hig_documents/SustainabilityReports'
DS_NORMATIVE_FOLDER='/hig_documents/efrag'
APP_LOCATION="global"
PRJ_LOCATION="us-central1"
# LLM Streaming default
STREAMING_MODE = False

# Pub Sub
TOPIC_ID = "gen-ai-pubsub-topic"
# Firestore
FIRESTORE_DATABASE_NAME = ''
FIRESTORE_COLLECTION_NAME = "basf-rag"
#API_ENDPOINT="1358703802.us-central1-1072008508617.vdb.vertexai.goog"
#INDEX_ENDPOINT="projects/1072008508617/locations/us-central1/indexEndpoints/6160664805498683392"
#DEPLOYED_INDEX_ID="company_data_1711154982110"
INDEX_ENDPOINT_ID = 'projects/1072008508617/locations/us-central1/indexEndpoints/6160664805498683392'
DEPLOYED_INDEX_ID = 'company_data_1711154982110'
# Must specify either `gcs_uri` or (`bigquery_dataset` and `bigquery_table`)
# Format: `gs://bucket/directory/object.json` or `gs://bucket/directory/*.json`
data_store_id = "sustainabilityreports2_1711047698168"
gcs_uri = "YOUR_GCS_PATH"
bigquery_dataset = "YOUR_BIGQUERY_DATASET"
bigquery_table = "YOUR_BIGQUERY_TABLE"
# https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/
CONFLUENCE_SPACE_NAMES =''
