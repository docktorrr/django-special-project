from django.core.management.base import BaseCommand, CommandError
from sp.users.models import UserProfile, recount_points

class Command(BaseCommand):

    def handle(self, *args, **options):
        for profile in UserProfile.objects.all():
            recount_points(profile)
