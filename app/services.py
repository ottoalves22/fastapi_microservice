from fastapi import HTTPException
import database

# Classe que interage com o banco, onde a lógica, processamentos etc são feitos

class DummyService:
    def hello_world():
        print('Hello world')

    def create():
        pass
        # salvar isso em algum db

    def get_one(id: int):
        pass

    def delete_one(id: int):
        pass

    def get_all():
        pass

    def update_one(id: int, text: str):
        pass