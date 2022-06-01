import traceback
from sqlalchemy import create_engine, Column, select, update, exc
from sqlalchemy.sql import func
from sqlalchemy.types import *
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import utils.configs as configs

db_string = f'postgresql://{configs.pg_user}:{configs.pg_pwd}@{configs.pg_host}:{str(configs.pg_port)}/{configs.pg_database}'
engine = create_engine(db_string)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()


class Dummy(Base):
    __tablename__ = 'Dummy'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    text = Column('text', String(128), default='')


Base.metadata.create_all(bind=engine)


def run_qry(statement, _type: str = 'all'):
    try:
        engine = create_engine(db_string, connect_args={'connect_timeout': 5})
        with Session(engine) as session:
            if _type == 'all':
                return session.execute(statement).scalars().all()
            
            return session.execute(statement).scalars().one()
    except exc.NoResultFound as e:
        return None


def get_all():
    try:
        statement = select(Dummy)
        return run_qry(statement=statement)
    except Exception as e:
        print(e)
        return None


def get_one(id: int):
    try:
        statement = select(Dummy).where(Dummy.id==id)
        return run_qry(statement=statement, _type='one')
    except Exception as e:
        print(e)
        return None


def save(obj):
    try:
        engine = create_engine(db_string)
        with Session(engine) as session:
            session.add(obj)
            session.commit()
            session.refresh(obj)
            return obj
    except AttributeError as r:
        traceback.print_exc()
        return r


def delete(id: int):
    statement = select(Dummy).filter_by(id=id)
    obj = run_qry(statement=statement, _type='one')

    try:
        engine = create_engine(db_string)
        with Session(engine) as session:
            session.delete(obj)
            session.commit()
    except:
        return None


def update(id: int, new_text: str):
    stmt = update(Dummy).where(Dummy.id == id).values(text=new_text)

    try:
        engine = create_engine(db_string)
        with Session(engine) as session:
            session.execute(stmt)
            session.commit()
            return True
    except Exception as e:
        print(e)
        return None
