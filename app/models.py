from pydantic import BaseModel, Field
from sqlalchemy import desc


class DummyOutputModel(BaseModel):
    id: int = Field(None, description='int id')


class DummyInputModel(BaseModel):
    text: str = Field(None, description='text')
        