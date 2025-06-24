from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='test@example.com', name='Test User', password='testpass')
        self.assertEqual(user.email, 'test@example.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create(email='test2@example.com', name='Test User2', password='testpass')
        team = Team.objects.create(name='Team A', members=[user.email])
        self.assertEqual(team.name, 'Team A')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(email='test3@example.com', name='Test User3', password='testpass')
        activity = Activity.objects.create(user_email=user.email, activity_type='run', duration=30)
        self.assertEqual(activity.activity_type, 'run')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = User.objects.create(email='test4@example.com', name='Test User4', password='testpass')
        team = Team.objects.create(name='Team B', members=[user.email])
        leaderboard = Leaderboard.objects.create(team_name=team.name, points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        self.assertEqual(workout.name, 'Pushups')
