from fastapi import FastAPI

from process_miner.api.routers import crawler, health, process

app = FastAPI(
    title="Process Miner API",
    description="API para extração e modelagem automática de processos",
    version="0.1.0",
)

app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(process.router, prefix="/processes", tags=["processes"])
app.include_router(crawler.router, prefix="/crawl", tags=["crawler"])
