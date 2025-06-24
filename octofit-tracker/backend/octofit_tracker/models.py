from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    # Add other fields as needed
    def __str__(self):
        return self.email

from djongo import models as djongo_models

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.JSONField(default=list)
    def __str__(self):
        return self.name


class Activity(models.Model):
    user_email = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user_email} - {self.activity_type}"


class Leaderboard(models.Model):
    team_name = models.CharField(max_length=100)
    points = models.IntegerField()
    def __str__(self):
        return f"{self.team_name} - {self.points}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name
