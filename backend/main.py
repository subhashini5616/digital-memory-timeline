from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

FILE = "events.json"


def read_events():
    with open(FILE, "r") as f:
        return json.load(f)


def write_events(events):
    with open(FILE, "w") as f:
        json.dump(events, f)


@app.get("/")
def home():
    return {"message": "Digital Memory Timeline API Running"}


# GET EVENTS
@app.get("/events")
def get_events():
    return read_events()


# CREATE EVENT
@app.post("/events")
def create_event(event: dict):

    events = read_events()

    event["id"] = len(events) + 1

    events.append(event)

    write_events(events)

    return event


# DELETE EVENT
@app.delete("/events/{event_id}")
def delete_event(event_id: int):

    events = read_events()

    events = [e for e in events if e["id"] != event_id]

    write_events(events)

    return {"message": "Event deleted"}