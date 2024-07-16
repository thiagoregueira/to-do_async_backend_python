# app/main.py
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app.api.v1.todos import todo
from app.core.config import settings

description_text = """
FastAPI TODO API
"""
app = FastAPI(
    title='FastAPI TODO ASYNC API',
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/', response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse(url='/docs')


@app.get('/ready', status_code=status.HTTP_200_OK, include_in_schema=True)
async def ready() -> str:
    """Check se a api está pronta para uso"""
    return 'ready'


app.include_router(
    todo.router,
    prefix='/api/v1/todos',
    tags=['todos'],
)
