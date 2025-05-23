# MongoDB models are not defined as Django ORM models, but you can define schemas for reference.

class User:
    def __init__(self, email, name, password, team_id=None):
        self.email = email
        self.name = name
        self.password = password
        self.team_id = team_id

class Team:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members or []

class Activity:
    def __init__(self, user_email, activity_type, duration, date, points):
        self.user_email = user_email
        self.activity_type = activity_type
        self.duration = duration
        self.date = date
        self.points = points

class Leaderboard:
    def __init__(self, team_name, points):
        self.team_name = team_name
        self.points = points

class Workout:
    def __init__(self, name, description, difficulty):
        self.name = name
        self.description = description
        self.difficulty = difficulty
