from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from db.db import meta

users = Table(
    'fast',meta,
    Column('id',Integer,primary_key=True),
    Column('name',String(255)),
    Column('mail',String(255)),
)