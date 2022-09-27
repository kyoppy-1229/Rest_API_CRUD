from sqlalchemy import create_engine, MetaData

# XAMPP上での実行コマンド
engine = create_engine("mysql+pymysql://root@localhost:3306/fastapi")

#ローカルでの実行コマンド
# engine = create_engine("mysql+pymysql://root:1229@localhost:3306/fastapi")

meta = MetaData()
conn = engine.connect()