from fastapi import FastAPI

from example_fastapi_sqlmodel_alembic.api.router import router

app = FastAPI()
app.include_router(router)
