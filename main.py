from fastapi import FastAPI,Response,HTTPException,status
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
import requests
import re

app=FastAPI()
app.add_middleware(HTTPSRedirectMiddleware)

@app.get("/addgroup",response_model=str,status_code=200)
async def addgroup(group,url,response:Response):
    """
    Add group name for your QuantumultX subscription

    args:

    - **group**: The group name you wang to add to the tags
    - **url**: The URL of your QuantumultX subscriprion, URLencode needed
    \f
    """
    try:
        res=requests.get(url)
        if res.status_code!=200:
            raise HTTPException(status_code=400,detail="check your url")
        res=str(res.content,encoding='UTF-8')
        res=re.sub("tag=","tag=%s "%group,res)
        return Response(res)
    except Exception as ex:
        raise HTTPException(status_code=500,detail=str(ex))
