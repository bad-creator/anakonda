from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def say_hallo():
    return "Hallo World"
