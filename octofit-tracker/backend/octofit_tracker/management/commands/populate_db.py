from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Borrar datos existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Crear usuarios
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', team=marvel),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='pass', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', password='pass', team=dc),
            User.objects.create_user(username='superman', email='superman@dc.com', password='pass', team=dc),
        ]

        # Crear actividades
        Activity.objects.create(user=users[0], type='run', duration=30, calories=300)
        Activity.objects.create(user=users[1], type='cycle', duration=45, calories=400)
        Activity.objects.create(user=users[2], type='swim', duration=60, calories=500)
        Activity.objects.create(user=users[3], type='walk', duration=20, calories=150)

        # Crear workouts
        Workout.objects.create(name='Full Body', description='Entrenamiento completo', duration=60)
        Workout.objects.create(name='Cardio Blast', description='Cardio intenso', duration=45)

        # Crear leaderboard
        Leaderboard.objects.create(user=users[0], score=1000)
        Leaderboard.objects.create(user=users[1], score=900)
        Leaderboard.objects.create(user=users[2], score=1100)
        Leaderboard.objects.create(user=users[3], score=950)

        self.stdout.write(self.style.SUCCESS('La base de datos octofit_db ha sido poblada con datos de prueba.'))
