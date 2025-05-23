from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from pymongo import MongoClient
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

mongo_host = settings.DATABASES['default']['CLIENT']['host']
mongo_port = settings.DATABASES['default']['CLIENT']['port']
mongo_db = settings.DATABASES['default']['NAME']
client = MongoClient(mongo_host, mongo_port)
db = client[mongo_db]

class UserList(APIView):
    def get(self, request):
        users = list(db.users.find({}, {"_id": 0}))
        return Response(users)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            db.users.insert_one(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeamList(APIView):
    def get(self, request):
        teams = list(db.teams.find({}, {"_id": 0}))
        return Response(teams)
    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            db.teams.insert_one(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActivityList(APIView):
    def get(self, request):
        activities = list(db.activity.find({}, {"_id": 0}))
        return Response(activities)
    def post(self, request):
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            db.activity.insert_one(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LeaderboardList(APIView):
    def get(self, request):
        leaderboard = list(db.leaderboard.find({}, {"_id": 0}))
        return Response(leaderboard)

class WorkoutList(APIView):
    def get(self, request):
        workouts = list(db.workouts.find({}, {"_id": 0}))
        return Response(workouts)
    def post(self, request):
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            db.workouts.insert_one(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
