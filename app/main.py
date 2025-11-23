from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import engine, Base
from app.api import stats, map, cluster

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Backend AI ML for Sorkorrearn")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(stats.router, prefix="/api")
app.include_router(map.router, prefix="/api")
app.include_router(cluster.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message":"Backend AI ML for Sorkorrearn"}
