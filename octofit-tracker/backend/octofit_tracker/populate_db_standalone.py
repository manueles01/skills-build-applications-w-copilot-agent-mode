from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['octofit_db']

# Users
db.users.delete_many({})
users = [
    {"email": "alice@example.com", "name": "Alice", "password": "alicepass", "team_id": "team1"},
    {"email": "bob@example.com", "name": "Bob", "password": "bobpass", "team_id": "team1"},
    {"email": "carol@example.com", "name": "Carol", "password": "carolpass", "team_id": "team2"},
]
db.users.insert_many(users)

# Teams
db.teams.delete_many({})
teams = [
    {"name": "Team 1", "members": ["alice@example.com", "bob@example.com"]},
    {"name": "Team 2", "members": ["carol@example.com"]},
]
db.teams.insert_many(teams)

# Activities
db.activity.delete_many({})
activities = [
    {"user_email": "alice@example.com", "activity_type": "run", "duration": 30, "date": "2025-05-23", "points": 10},
    {"user_email": "bob@example.com", "activity_type": "walk", "duration": 60, "date": "2025-05-23", "points": 8},
    {"user_email": "carol@example.com", "activity_type": "cycle", "duration": 45, "date": "2025-05-23", "points": 12},
]
db.activity.insert_many(activities)

# Leaderboard
db.leaderboard.delete_many({})
leaderboard = [
    {"team_name": "Team 1", "points": 18},
    {"team_name": "Team 2", "points": 12},
]
db.leaderboard.insert_many(leaderboard)

# Workouts
db.workouts.delete_many({})
workouts = [
    {"name": "Pushups", "description": "Do 20 pushups", "difficulty": "Easy"},
    {"name": "Situps", "description": "Do 30 situps", "difficulty": "Medium"},
]
db.workouts.insert_many(workouts)

print('Test data populated in octofit_db.')
