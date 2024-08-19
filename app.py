import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return 'API Home Page'

@app.get('/hello')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    uvicorn.run(app)