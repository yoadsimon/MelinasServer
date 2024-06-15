# MelinasServer

MelinasServer for sending emails after every update.

## Setup and Deployment

Before deploying, make sure to load your environment variables:

```sh

export $(grep -v '^#' .env | xargs)
```

To deploy the `sendEmailFunction` on Google Cloud Functions, use the following command:

```sh
gcloud functions deploy sendEmailFunction \
    --runtime python311 \
    --trigger-http \
    --allow-unauthenticated \
    --entry-point entry_point \
    --set-env-vars GMAIL_USER="$GMAIL_USER",GMAIL_PASSWORD="$GMAIL_PASSWORD"
```


## Testing the Server
```sh
curl -m 70 -X POST https://us-central1-melinas-server.cloudfunctions.net/sendEmailFunction/send-email \
    -H "Content-Type: application/json" \
    -d '{
        "subject": "Test Email",
        "message": "This is a test email from the Google Cloud Function"
    }'
```
