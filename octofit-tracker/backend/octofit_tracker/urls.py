"""
URL configuration for octofit_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserList, TeamList, ActivityList, LeaderboardList, WorkoutList
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        "users": request.build_absolute_uri("/users/"),
        "teams": request.build_absolute_uri("/teams/"),
        "activity": request.build_absolute_uri("/activity/"),
        "leaderboard": request.build_absolute_uri("/leaderboard/"),
        "workouts": request.build_absolute_uri("/workouts/"),
    })

urlpatterns = format_suffix_patterns([
    path("admin/", admin.site.urls),
    path("", api_root, name="api-root"),
    path("users/", UserList.as_view(), name="user-list"),
    path("teams/", TeamList.as_view(), name="team-list"),
    path("activity/", ActivityList.as_view(), name="activity-list"),
    path("leaderboard/", LeaderboardList.as_view(), name="leaderboard-list"),
    path("workouts/", WorkoutList.as_view(), name="workout-list"),
])
