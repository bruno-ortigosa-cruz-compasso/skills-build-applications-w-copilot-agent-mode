from django.core.management.base import BaseCommand
from django.conf import settings
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Users (using Django's User model which requires username)
        users = [
            User.objects.create_user(username='tonystark', email='tony@stark.com', first_name='Tony', last_name='Stark'),
            User.objects.create_user(username='steverogers', email='steve@rogers.com', first_name='Steve', last_name='Rogers'),
            User.objects.create_user(username='clarkkent', email='clark@kent.com', first_name='Clark', last_name='Kent'),
            User.objects.create_user(username='dianaprince', email='diana@prince.com', first_name='Diana', last_name='Prince'),
        ]

        # Teams
        marvel = Team.objects.create(name='Marvel', member_ids=[str(users[0].pk), str(users[1].pk)])
        dc = Team.objects.create(name='DC', member_ids=[str(users[2].pk), str(users[3].pk)])

        # Activities
        activities = [
            Activity(user_id=str(users[0].pk), user_username=users[0].username, type='Running', duration=30, calories=300, date=date.today()),
            Activity(user_id=str(users[1].pk), user_username=users[1].username, type='Cycling', duration=45, calories=450, date=date.today()),
            Activity(user_id=str(users[2].pk), user_username=users[2].username, type='Swimming', duration=60, calories=600, date=date.today()),
            Activity(user_id=str(users[3].pk), user_username=users[3].username, type='Yoga', duration=50, calories=250, date=date.today()),
        ]
        Activity.objects.bulk_create(activities)

        # Leaderboard
        Leaderboard.objects.create(team_id=str(marvel.pk), team_name=marvel.name, score=750)
        Leaderboard.objects.create(team_id=str(dc.pk), team_name=dc.name, score=850)

        # Workouts
        workouts = [
            Workout(name='Iron Man HIIT', description='High-intensity interval training', difficulty='Hard', suggested_for='Advanced athletes'),
            Workout(name='Superman Strength', description='Full body strength training', difficulty='Hard', suggested_for='Advanced athletes'),
            Workout(name='Captain America Cardio', description='Cardiovascular endurance training', difficulty='Medium', suggested_for='Intermediate'),
            Workout(name='Wonder Woman Flex', description='Flexibility and balance', difficulty='Medium', suggested_for='All levels'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
