# apis written with Python and [FastAPI](https://github.com/tiangolo/fastapi)

You can visit [here](https://api.emonq.com/docs) to see the demo

## Features

   - [x] **addgroup**: Add group name for QuantumultX subscriptions to avoid nodes confliction.
   - [x] **ddns**: Work as a proxy to Google DDNS

## Usage
   1. Install requirements with 
      
      > `pip install -r requirements.txt`
   2. Run
      
       > gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
