from fastapi import FastAPI

app = FastAPI(title="Platform API")

@app.get("/")
def read_root():
    return {
        "service": "Platform API is running",
        "status": "Healthy"
        }

@app.get("/health")
def health():
    return {
        "status": "OK"
        }