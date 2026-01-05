
from fastapi import FastAPI

from app.api import auth


app = FastAPI(title="AgentOps Platform")


app.include_router(auth.router)

@app.get("/health")
async def health():
    return {"status": "ok"}
