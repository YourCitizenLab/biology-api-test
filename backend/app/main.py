from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers import cards, chat, evidence, simulate

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Concept-level AI Bio/Chem Discovery Simulator backend.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_origin, "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": settings.service_name}


app.include_router(simulate.router, prefix="/api")
app.include_router(evidence.router, prefix="/api")
app.include_router(chat.router, prefix="/api")
app.include_router(cards.router, prefix="/api")
