import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return 'API home page...'

@app.get('/hello')
def hello():
    return 'Hello World!'