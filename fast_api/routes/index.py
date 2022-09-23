from fastapi import APIRouter
from db.db import conn
from models.index import users
from schemas.index import User

user = APIRouter()

# 全件表示
@user.get("/user")
async def read_data():
    return conn.execute(users.select()).fetchall()

# 指定のIDの表示
@user.get("/user/{id}")
async def read_data(id: int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall()

# 新しいデータの作成
@user.post("/user")
async def write_data(user: User):
    conn.execute(users.insert().values(
        name=user.name,
        mail=user.mail
    ))
    return conn.execute(users.select()).fetchall()

# 既存データのアップデート
@user.put("/user/{id}")
async def update_data(id:int, user: User):
    conn.execute(users.update().values(
        name=user.name,
        mail=user.mail
    ).where(users.c.id == id))
    return conn.execute(users.select()).fetchall()

# データの削除
@user.delete("/user/{id}")
async def delete_data(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select()).fetchall()