from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate octofit_db with test data.'

    def handle(self, *args, **kwargs):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']

        # Users
        users = [
            {"email": "alice@example.com", "name": "Alice", "password": "alicepass", "team_id": "team1"},
            {"email": "bob@example.com", "name": "Bob", "password": "bobpass", "team_id": "team1"},
            {"email": "carol@example.com", "name": "Carol", "password": "carolpass", "team_id": "team2"},
        ]
        db.users.delete_many({})
        db.users.insert_many(users)
        db.users.create_index({"email": 1}, unique=True)

        # Teams
        teams = [
            {"name": "Team 1", "members": ["alice@example.com", "bob@example.com"]},
            {"name": "Team 2", "members": ["carol@example.com"]},
        ]
        db.teams.delete_many({})
        db.teams.insert_many(teams)
        db.teams.create_index({"name": 1}, unique=True)

        # Activities
        activities = [
            {"activity_id": 1, "user_email": "alice@example.com", "activity_type": "run", "duration": 30, "date": "2025-05-23", "points": 10},
            {"activity_id": 2, "user_email": "bob@example.com", "activity_type": "walk", "duration": 60, "date": "2025-05-23", "points": 8},
            {"activity_id": 3, "user_email": "carol@example.com", "activity_type": "cycle", "duration": 45, "date": "2025-05-23", "points": 12},
        ]
        db.activity.delete_many({})
        db.activity.insert_many(activities)
        db.activity.create_index({"activity_id": 1}, unique=True)

        # Leaderboard
        leaderboard = [
            {"leaderboard_id": 1, "team_name": "Team 1", "points": 18},
            {"leaderboard_id": 2, "team_name": "Team 2", "points": 12},
        ]
        db.leaderboard.delete_many({})
        db.leaderboard.insert_many(leaderboard)
        db.leaderboard.create_index({"leaderboard_id": 1}, unique=True)

        # Workouts
        workouts = [
            {"workout_id": 1, "name": "Pushups", "description": "Do 20 pushups", "difficulty": "Easy"},
            {"workout_id": 2, "name": "Situps", "description": "Do 30 situps", "difficulty": "Medium"},
        ]
        db.workouts.delete_many({})
        db.workouts.insert_many(workouts)
        db.workouts.create_index({"workout_id": 1}, unique=True)

        self.stdout.write(self.style.SUCCESS('Test data and indexes populated in octofit_db.'))
