import fastapi

app = fastapi.FastAPI()


@app.get("/hello")
def hello():
    return {"message": "hello"}
