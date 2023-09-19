import os
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from backend.src.database import ObjetoSQL
import json

rotas = APIRouter()
templates_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'utils')
templates = Jinja2Templates(directory=templates_path)


def criar_saida(content, message=''):
    return {"message": message,
            "content": content}


@rotas.get(path="/",
           responses={200: {"description": "Ok", "content": {"image/jpeg": {"example": "pagina"}}},
                      400: {"description": "not found"}},
           tags=["Home"],
           name="Página inicial",
           description="Apresenta página inicial do projeto")
async def home(request: Request):
    """
        Função que renderiza a página estática home.
        :returns: Página inicial
        :rtype: fastapi.Request
        """
    return templates.TemplateResponse("index.html", {"request": request})

@rotas.get(path="/story",
           responses={200: {"message": "Ok", "content": ""},
                      400: {"description": "not found"}},
           tags=["story"],
           name="story",
           description="Consulta Histórias")
async def story():
    """
    Função que consulta uma tabela no Supabase.
    :returns: Lista de conteúdo devolvida pela query
    :rtype:
    """
    supa_cliente = ObjetoSQL()
    dados = supa_cliente.processar_query_select(tabela='story')
    print(dados)
    return criar_saida(dados)


@rotas.get(path="/task",
           responses={200: {"message": "Ok", "content": ""},
                      400: {"description": "not found"}},
           tags=["task"],
           name="task",
           description="Consulta Tarefas")
async def story():
    """
    Função que consulta uma tabela no Supabase.
    :returns: Lista de conteúdo devolvida pela query
    :rtype:
    """
    supa_cliente = ObjetoSQL()
    dados = supa_cliente.processar_query_select(tabela='task')
    print(dados)
    return criar_saida(dados)


@rotas.post(path="/story",
            responses={201: {"description": "Created", "content": ""},
                       400: {"description": "not found"}},
            tags=["story"],
            name="Insert story",
            description="Alimentar Tabela Story")
async def post_story(request: dict):
    """
    Função que renderiza a página estática home.
    :returns: Página inicial
    :rtype: fastapi.Request
    """
    supa_cliente = ObjetoSQL()
    print(request, type(request))
    operation = request.get('operation')
    if operation.upper() == 'INSERT':
        dados = supa_cliente.processar_query_insert(tabela='story', dados=request.get('data'))
    elif operation.upper() == 'UPDATE':
        dados = supa_cliente.processar_query_update(tabela='story', dados=request.get('data'))
    elif operation.upper() == 'DELETE':
        dados = supa_cliente.processar_query_delete(tabela='story', dados=request.get('data'))
    return criar_saida(dados)


@rotas.post(path="/task",
            responses={201: {"description": "Created", "content": ""},
                       400: {"description": "not found"}},
            tags=["task"],
            name="Insert task",
            description="Alimentar Tabela task")
async def post_story(request: dict):
    """
    Função que renderiza a página estática home.
    :returns: Página inicial
    :rtype: fastapi.Request
    """
    supa_cliente = ObjetoSQL()
    print(request, type(request))
    operation = request.get('operation')
    if operation.upper() == 'INSERT':
        dados = supa_cliente.processar_query_insert(tabela='task', dados=request.get('data'))
    elif operation.upper() == 'UPDATE':
        dados = supa_cliente.processar_query_update(tabela='task', dados=request.get('data'))
    elif operation.upper() == 'DELETE':
        dados = supa_cliente.processar_query_delete(tabela='task', dados=request.get('data'))
    return criar_saida(dados)