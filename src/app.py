"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Team practices and inter-school soccer matches",
        "schedule": "Mondays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 22,
        "participants": ["liam@mergington.edu", "noah@mergington.edu"]
    },
    "Basketball Club": {
        "description": "Basketball drills, scrimmages, and league preparation",
        "schedule": "Tuesdays and Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["ava@mergington.edu", "isabella@mergington.edu"]
    },
    "Drama Club": {
        "description": "Acting workshops and school theater productions",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["mia@mergington.edu", "charlotte@mergington.edu"]
    },
    "Art Studio": {
        "description": "Drawing, painting, and mixed-media art projects",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 16,
        "participants": ["amelia@mergington.edu", "harper@mergington.edu"]
    },
    "Debate Team": {
        "description": "Public speaking, argumentation, and debate competitions",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 14,
        "participants": ["elijah@mergington.edu", "james@mergington.edu"]
    },
    "Science Olympiad": {
        "description": "STEM challenges, experiments, and academic competitions",
        "schedule": "Wednesdays and Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": ["benjamin@mergington.edu", "lucas@mergington.edu"]
    },
    "Tennis Club": {
        "description": "Tennis training, drills, and tournaments",
        "schedule": "Tuesdays and Saturdays, 4:00 PM - 5:30 PM",
        "max_participants": 12,
        "participants": ["alexander@mergington.edu"]
    },
    "Swimming Team": {
        "description": "Competitive swimming and relay training",
        "schedule": "Mondays, Wednesdays, Fridays, 4:00 PM - 5:15 PM",
        "max_participants": 25,
        "participants": ["grace@mergington.edu", "zoe@mergington.edu"]
    },
    "Music Band": {
        "description": "Play instruments and perform in school concerts",
        "schedule": "Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 30,
        "participants": ["lily@mergington.edu"]
    },
    "Photography Club": {
        "description": "Learn photography techniques and digital editing",
        "schedule": "Wednesdays, 4:00 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["ethan@mergington.edu", "mason@mergington.edu"]
    },
    "Model United Nations": {
        "description": "Participate in diplomatic simulations and international debates",
        "schedule": "Fridays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["hannah@mergington.edu"]
    },
    "Robotics Club": {
        "description": "Design, build, and program robots for competitions",
        "schedule": "Tuesdays and Thursdays, 4:30 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["jacob@mergington.edu", "logan@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Check if student is already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up for this activity")  
    

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
