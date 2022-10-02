from fastapi import FastAPI
import uvicorn
from src.logic import ask_arun, list_arun, make_phrase

app = FastAPI()


@app.get("/")
async def home():
    return {"Message": "Welcome to ask_arun web app by using seach and list"}


@app.get("/search/{value}")
async def search(value: str):
    result = list_arun(value)
    return {"search result": result}


@app.get("/ask_arun/{value}")
async def ask(value: str):
    result = ask_arun(value)
    return {"output": result}


@app.get("/phrase_it/{value}")
async def phrase_para(value: str):
    result = make_phrase(value)
    return {"output": result}


if __name__ == "__main__":
    uvicorn.run(app, port="8080", host="0.0.0.0")
