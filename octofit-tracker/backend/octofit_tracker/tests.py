from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_create_user(self):
        response = self.client.post(reverse('user-list'), {'email': 'test@example.com', 'name': 'Test', 'password': 'pass'})
        self.assertEqual(response.status_code, 201)

class TeamTests(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_create_team(self):
        response = self.client.post(reverse('team-list'), {'name': 'TeamA'})
        self.assertEqual(response.status_code, 201)

class ActivityTests(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_create_activity(self):
        response = self.client.post(reverse('activity-list'), {'user_email': 'test@example.com', 'activity_type': 'run', 'duration': 30, 'date': '2025-05-23', 'points': 10})
        self.assertEqual(response.status_code, 201)

class LeaderboardTests(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_get_leaderboard(self):
        response = self.client.get(reverse('leaderboard-list'))
        self.assertEqual(response.status_code, 200)

class WorkoutTests(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_create_workout(self):
        response = self.client.post(reverse('workout-list'), {'name': 'Pushups', 'description': 'Do pushups', 'difficulty': 'Easy'})
        self.assertEqual(response.status_code, 201)
