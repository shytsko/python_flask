import datetime

from databases import Database
from sqlalchemy import MetaData, Table, Integer, String, Column, create_engine, Text, DECIMAL, Date, ForeignKey
from settings import settings

DATABASE_URL = settings.DATABASE_URL
database = Database(DATABASE_URL)
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("firstname", String(32), nullable=False),
    Column("lastname", String(32), nullable=False),
    Column("email", String(128), nullable=False),
    Column("password", String(128), nullable=False)
)

goods = Table(
    "goods",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(32), nullable=False),
    Column("description", Text(), nullable=False),
    Column("price", DECIMAL(10, 2), default=0)
)

orders = Table(
    "orders",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("date", Date(), default=datetime.datetime.now()),
    Column("user_id", ForeignKey("users.id")),
    Column("good_id", ForeignKey("goods.id"))
)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# metadata.drop_all()
metadata.create_all(engine)
