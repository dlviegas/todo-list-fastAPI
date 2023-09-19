from backend.src.application import api
from backend.src.rotas import rotas
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost:80",
    "localhost:80"
]

@api.on_event('startup')
def __startup():
    """
    Inicialização da API
    """
    print(f'Iniciando - API')


@api.on_event('shutdown')
def __shutdown():
    """
    O que fazer quando a API é encerrada
    """
    print(f'Encerrando - API')


api.include_router(rotas)
api.mount("/static", StaticFiles(
        directory="backend/src/static"), name="static")

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
