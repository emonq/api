# apis written with Python and [FastAPI](https://github.com/tiangolo/fastapi)
**Demo**: https://api.emonq.com:8000

Read api docs [HERE](https://api.emonq.com:8000/docs)

## Futures
   - [x] **addgroup**: Add group name for QuantumultX subscriptions to avoid nodes confliction.

   More are coming soon...
## Usage
   1. Install requirements with 
      > `pip install -r requirements.txt`
   2. Run with uvicorn
       > `uvicorn main:app --host 0.0.0.0 --ssl-keyfile <yourkeyfile> --ssl-certfile <yourcertfile>`
