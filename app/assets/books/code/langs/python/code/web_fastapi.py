# FAST API 
'''
Fast (high-performance) web framework to build APIs on Python >= 3.6+ based on standard Python type hints.
Every developer in my network has shifted to FastApi from Django and Flask. 
It is a lot easier to learn and quick to implement. The performance is as par with Golang and Node. 

Asynchronous tasks are integrated by default. Flask does have support for asynchronous tasks, but the “celery” module needs 
to be imported. Same thing when it comes to sending responses in Flask (“json” module is needed). FastAPI by 
default sends responses as JSON objects. Finally, the swagger documentation is amazing! 

pip install fastapi
'''

from fastapi import FastAPI
from pydantic import BaseModel  # data validation

class User(BaseModel):
    email: str
    password: str

app = FastAPI()

@app.post("/login")
def login(user: User):
    # ...
    # do some magic
    # ...
    return {"msg": "login successful"}

print('Listening...')

# To run, serve with uvicorn: uvicorn main:app
# https://www.uvicorn.org/
# curl -X POST "http://localhost:8000/login" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"email\":\"string\",\"password\":\"string\"}"







>pip3 install fastapi
pip3 install uvicorn
pip3 install pydantic

```python
app = FastAPI(
    title = "Logging API",
    description = "An API for all your logging needs.",
    version = "2.0",
)

@app.get("/loggingapi/v2/logs/{appId}")
async def Logs(appId: str):
    results = storage.GetLogs(appId)
    return results    

GET request — /loggingapi/v1/logs
 
POST request — /loggingapi/v1/log    
{
     "appId": 7542a72b-b6eb-4b9d-a672-a8d82ad0dadf
     "message": "This is my log message."
}    
```
    

### More
- https://py.plainenglish.io/abandoning-flask-for-fastapi-20105948b062
- https://github.com/tiangolo/fastapi
- https://towardsdatascience.com/you-should-start-using-fastapi-now-7efb280fec02
- https://py.plainenglish.io/abandoning-flask-for-fastapi-20105948b062