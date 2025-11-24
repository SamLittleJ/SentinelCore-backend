from fastapi import FastAPI

app = FastAPI(title="SentinelCore API", version="0.1.0")

@app.get("/health", tags=["System"])
async def healthcheck():
    return {
        "status": "ok",
        "service": "SentinelCore Backend",
        "version": "0.1.0"
            }