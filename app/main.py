from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "API rodando "}

@app.get("/health")
def health_check():
    return {"status": "ok"}
