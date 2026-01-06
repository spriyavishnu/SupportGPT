
from fastapi import FastAPI

from app.api import auth
from app.api import users


app = FastAPI(title="AgentOps Platform")


app.include_router(auth.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Welcome to AgentOps Platform", "docs": "/docs"}

@app.get("/health")
async def health():
    return {"status": "ok"}
