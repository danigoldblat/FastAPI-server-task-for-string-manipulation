from string_ops import (reverse_str, to_upper, remove_vowels)
from fastapi import FastAPI
import uvicorn
app = FastAPI()


@app.get("/reverse")
def reverse_server(text:str):
    a=reverse_str(text)
    return {"orignl":text ,"reverse_text":a}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)