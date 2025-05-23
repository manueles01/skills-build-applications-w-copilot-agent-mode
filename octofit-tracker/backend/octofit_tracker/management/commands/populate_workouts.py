from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate MongoDB with sample workout data for testing.'

    def handle(self, *args, **kwargs):
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'], settings.DATABASES['default']['CLIENT']['port'])
        db = client[settings.DATABASES['default']['NAME']]

        workouts = [
            {"name": "Pushups", "description": "Do 20 pushups", "difficulty": "Easy"},
            {"name": "Situps", "description": "Do 30 situps", "difficulty": "Medium"},
            {"name": "Squats", "description": "Do 15 squats", "difficulty": "Easy"},
            {"name": "Plank", "description": "Hold plank for 1 minute", "difficulty": "Medium"},
            {"name": "Burpees", "description": "Do 10 burpees", "difficulty": "Hard"},
        ]
        db.workouts.delete_many({})
        db.workouts.insert_many(workouts)
        self.stdout.write(self.style.SUCCESS('Sample workout data populated in MongoDB.'))
