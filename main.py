from fastapi import FastAPI,Response,HTTPException,status,Request
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
        return res
    except Exception as ex:
        raise HTTPException(status_code=500,detail=str(ex))

@app.get("/ddns")
async def ddns(username:str,password:str,domain:str,request:Request,response:Response,ip:str=None):
    """
    Update Google DDNS for somewhere cannot visit Google

    args:

    - **username**
    - **password**
    - **domain**
    - **ip**
    \f
    """
    if ip==None:
        try:
            ip=request.headers['X-Forwarded-For'].split(',')[0]
        except Exception as ex:
            ip=request.client.host
    try:
        res=requests.post(
            url="https://%s:%s@domains.google.com/nic/update"%(username,password),
            data={"hostname":domain,"myip":ip},
            headers={"User-Agent":"myddns","Authorization":"Basic base64-encoded-auth-string"}
            )
        return str(res.content,encoding='UTF-8')
    except Exception as ex:
        raise HTTPException(status_code=500,detail=str(ex))
