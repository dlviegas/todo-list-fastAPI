from fastapi import FastAPI

api = FastAPI(version='0.0.1', docs_url='/docs', redoc_url='/redoc', title="ToDo List")
