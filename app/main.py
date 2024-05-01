from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, text

engine = create_engine('sqlite:///announcements.db')
meta = MetaData()

announcements_table = Table('announcements', meta,
    Column('id', Integer, primary_key=True),
    Column('content', String),
    Column('scheduled_time', DateTime)
)

meta.create_all(engine)

class Announcement(BaseModel):
    id: int
    content: str
    scheduled_time: datetime

engine = create_engine('sqlite:///announcements.db')

# Define a route to schedule an announcement
@app.post("/schedule_announcement")
async def schedule_announcement(announcement: dict):
    with engine.connect() as connection:
        # Insert the announcement into the database
        connection.execute(text("INSERT INTO announcements (content, scheduled_time) VALUES (:content, :scheduled_time)"),
                   announcement)
    return {"message": "Announcement scheduled"}

# Define a route to send announcements
@app.get("/send_announcements")
async def send_announcements():
    with engine.connect() as connection:
        # Retrieve announcements from the database
        announcements = connection.execute(text("SELECT * FROM announcements WHERE scheduled_time <= CURRENT_TIMESTAMP")).fetchall()
        # Send the announcements (simulated)
        for announcement in announcements:
            print(f"Sending announcement {(announcement.id)}: {announcement.content}")
    return {"message": "Announcements sent"}

# Define a route to view scheduled announcements
@app.get("/scheduled_announcements")
async def scheduled_announcements():
    with engine.connect() as connection:
        # Retrieve scheduled announcements from the database
        scheduled_announcements = connection.execute(text("SELECT * FROM announcements WHERE scheduled_time >= CURRENT_TIMESTAMP")).fetchall()
    return {"scheduled_announcements": scheduled_announcements}
