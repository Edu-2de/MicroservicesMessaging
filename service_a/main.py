from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Service A is running!"}