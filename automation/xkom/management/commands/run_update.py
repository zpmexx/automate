from django.core.management.base import BaseCommand
import subprocess

class Command(BaseCommand):
    help = 'Runs the update.py script'

    def handle(self, *args, **kwargs):
        subprocess.run(['python', 'update.py'], check=True)