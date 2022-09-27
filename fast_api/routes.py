from fastapi import APIRouter
from db import conn
from models import users
from schemas import User

user = APIRouter(prefix='/user', tags=['user'])

# 全件表示
@user.get("/")
async def read_data():
    return conn.execute(users.select()).fetchall()

# 指定のIDのみ検索
@user.get("/{id}")
async def read_data(id: int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall()

# 新しいデータの作成
@user.post("/")
async def write_data(user: User):
    conn.execute(users.insert().values(
        name=user.name,
        mail=user.mail
    ))
    return conn.execute(users.select()).fetchall()

# 既存データのアップデート
@user.put("/{id}")
async def update_data(id:int, user: User):
    conn.execute(users.update().values(
        name=user.name,
        mail=user.mail
    ).where(users.c.id == id))
    return conn.execute(users.select()).fetchall()

# データの削除
@user.delete("/{id}")
async def delete_data(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select()).fetchall()