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
            response.status_code=status.HTTP_400_BAD_REQUEST
        res=str(res.content,encoding='UTF-8')
        res=re.sub("tag=","tag=%s "%group,res)
        return Response(res, media_type="application/text")
    except Exception as ex:
        response.status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
