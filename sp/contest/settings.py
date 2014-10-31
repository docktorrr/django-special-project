from django.conf import settings

ACTIVE_CONTEST = getattr(settings, 'ACTIVE_CONTEST', 1)
