import asyncio
from app.db.base import Base
from app.db.session import engine

async def init_db():
    # Create tables using the async engine
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    await engine.dispose()
    print("✓ Database tables created successfully!")

if __name__ == "__main__":
    asyncio.run(init_db())
