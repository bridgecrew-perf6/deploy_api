import datetime
from fastapi import FastAPI
# バリデーション周り
from pydantic import BaseModel, Field


class Booking(BaseModel):
    booking_id: int
    user_id: int
    room_id: int
    booked_num: int
    start_datetime: datetime.datetime  # 時間日付を扱える型
    end_datetime: datetime.datetime


class User(BaseModel):
    user_id: int
    username: str = Field(max_length=12)


class Room(BaseModel):
    room_id: int
    room_name: str = Field(max_length=12)
    capacity: int


app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Success"}


@app.post("/users")
async def users(users: User):
    return {"users": users}


@app.post("/rooms")
async def users(rooms: Room):
    return {"rooms": rooms}


@app.post("/booking")
async def users(booking: Booking):
    return {"booking": booking}
