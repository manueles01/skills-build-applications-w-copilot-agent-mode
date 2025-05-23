from django.core.management.base import BaseCommand

# Added by Copilot agent mode for Mona compliance
from pymongo import MongoClient
from django.conf import settings

class Command(BaseCommand):
    help = 'Populate octofit_db with test data.'

    def handle(self, *args, **kwargs):
        # Use settings from Django for Mona compliance
        db_settings = settings.DATABASES['default']
        client = MongoClient(db_settings['HOST'], db_settings['PORT'])
        db = client[db_settings['NAME']]

        # Users
        users = [
            {"email": "alice@example.com", "name": "Alice", "password": "alicepass", "team_id": "team1"},
            {"email": "bob@example.com", "name": "Bob", "password": "bobpass", "team_id": "team1"},
            {"email": "carol@example.com", "name": "Carol", "password": "carolpass", "team_id": "team2"},
        ]
        db.users.delete_many({})
        db.users.insert_many(users)
        db.users.create_index([("email", 1)], unique=True)

        # Teams
        teams = [
            {"name": "Team 1", "members": ["alice@example.com", "bob@example.com"]},
            {"name": "Team 2", "members": ["carol@example.com"]},
        ]
        db.teams.delete_many({})
        db.teams.insert_many(teams)
        db.teams.create_index([("name", 1)], unique=True)

        # Activities
        activities = [
            {"user_email": "alice@example.com", "activity_type": "run", "duration": 30, "date": "2025-05-23", "points": 10},
            {"user_email": "bob@example.com", "activity_type": "walk", "duration": 60, "date": "2025-05-23", "points": 8},
            {"user_email": "carol@example.com", "activity_type": "cycle", "duration": 45, "date": "2025-05-23", "points": 12},
        ]
        db.activity.delete_many({})
        db.activity.insert_many(activities)

        # Leaderboard
        leaderboard = [
            {"team_name": "Team 1", "points": 18},
            {"team_name": "Team 2", "points": 12},
        ]
        db.leaderboard.delete_many({})
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            {"name": "Pushups", "description": "Do 20 pushups", "difficulty": "Easy"},
            {"name": "Situps", "description": "Do 30 situps", "difficulty": "Medium"},
        ]
        db.workouts.delete_many({})
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Test data populated in octofit_db.'))
