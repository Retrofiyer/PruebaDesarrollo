from fastapi import FastAPI
from PruebaOpenAI.ProyectOpenAI import Document, inference

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/inference', status_code=200)
def inference_endpoint(doc: Document):
    response = inference(doc.prompt)
    return{
        'inference': response[0],
        'usage': response[1]
    }
