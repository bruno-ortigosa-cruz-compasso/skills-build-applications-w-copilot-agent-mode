from djongo import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Extend as needed
    pass

class Team(models.Model):
    name = models.CharField(max_length=100)
    member_ids = models.JSONField(default=list)  # Store user IDs as list
    created_at = models.DateTimeField(auto_now_add=True)

class Activity(models.Model):
    user_id = models.CharField(max_length=100)  # Store User ID as string
    user_username = models.CharField(max_length=150, default='')  # Cache username for easier display
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # minutes
    calories = models.IntegerField()
    date = models.DateField()

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    suggested_for = models.CharField(max_length=100)

class Leaderboard(models.Model):
    team_id = models.CharField(max_length=100)  # Store Team ID as string
    team_name = models.CharField(max_length=100, default='')  # Cache team name for easier display
    score = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
