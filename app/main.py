from typing import List
import models
from .services import DummyService
from fastapi import FastAPI, Depends, Query, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security.http import HTTPBearer, HTTPBasicCredentials

description = """
🚀dummy🚀

### dummy

"""

app = FastAPI(title='Dummy Api',
              description=description,
              version='1.0.0',
              openapi_url='/dummy/openapi.json',
              docs_url='/dummy/docs',
              redoc_url='/dummy/redoc'
              )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    global dummy_svc
    dummy_svc = DummyService()


@app.post('/dummy',
          tags=['test_function'],
          description="",
          responses={
              200: {
                  "description": "Returns the object.",
              }
          },
          response_model=models.DummyOutputModel
          )
async def create():
    global dummy_svc
    new = dummy_svc.create()
    return models.DummyOutputModel(id=new.id)


@app.get('/dummy/{id}',
         tags=['test_function'],
         description="Get an existing dummy by id.",
         responses={
             200: {
                 "description": "Returns the object.",
             }
         },
         response_model=models.DummyOutputModel
         )
async def get_one(id: int):
    global dummy_svc
    res = dummy_svc.get_one(id)
    return models.DummyOutputModel(id=res.id)


@app.delete('/dummy/{id}',
            tags=['test_function'],
            description="Deletes an existing dummy by id.",
            responses={
                200: {
                    "description": "Returns true if the operation was completed with success.",
                },
                404: {
                    "description": "Process not found.",
                }
            },
            response_model=bool
            )
async def delete_one(id: int):
    global dummy_svc
    return dummy_svc.delete_one(id)


@app.get('/dummy',
         tags=['test_function'],
         description="Get all dummies",
         responses={
             200: {
                 "description": "Returns all the dummy objects.",
             }
         },
         response_model=List[models.DummyOutputModel]
         )
async def get_all():
    global dummy_svc
    results = dummy_svc.get_all()
    if results is not None:
        return [models.DummyOutputModel(id=res.id) for res in results]
    else:
        return []


@app.put('/dummy/{id}',
         tags=['test_function'],
         description="Update one dummy",
         responses={
             200: {
                 "description": "Update an dummy object.",
             }
         },
         response_model=models.DummyOutputModel
         )
async def update_one(id: int, model: models.DummyInputModel):
    global dummy_svc
    res = dummy_svc.update_one(id, model.text)
    return models.DummyOutputModel(id=res.id)
