def test_signup_success(client):
    # choose an activity that exists and an email not present
    activity = "Tennis Club"
    email = "newstudent@mergington.edu"

    resp = client.post(f"/activities/{activity}/signup?email={email}")
    assert resp.status_code == 200
    data = resp.json()
    assert "Signed up" in data["message"]

    # Ensure the participant appears in the activities payload
    activities = client.get("/activities").json()
    assert email in activities[activity]["participants"]


def test_signup_duplicate(client):
    activity = "Chess Club"
    # use an existing participant from the initial dataset
    email = "michael@mergington.edu"

    # First attempt should return 400 because already signed up
    resp = client.post(f"/activities/{activity}/signup?email={email}")
    assert resp.status_code == 400


def test_signup_invalid_activity(client):
    resp = client.post("/activities/Nonexistent%20Club/signup?email=foo@x.com")
    assert resp.status_code == 404


def test_unregister_success(client):
    activity = "Basketball Club"
    email = "ava@mergington.edu"

    # ensure present initially
    activities_before = client.get("/activities").json()
    assert email in activities_before[activity]["participants"]

    resp = client.delete(f"/activities/{activity}/unregister?email={email}")
    assert resp.status_code == 200
    data = resp.json()
    assert "Unregistered" in data["message"]

    activities_after = client.get("/activities").json()
    assert email not in activities_after[activity]["participants"]


def test_unregister_not_signed(client):
    activity = "Science Olympiad"
    email = "not-registered@mergington.edu"

    resp = client.delete(f"/activities/{activity}/unregister?email={email}")
    assert resp.status_code == 404


def test_unregister_invalid_activity(client):
    resp = client.delete("/activities/NoActivity/unregister?email=foo@x.com")
    assert resp.status_code == 404
