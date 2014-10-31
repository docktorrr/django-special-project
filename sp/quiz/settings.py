from django.conf import settings

ACTIVE_QUIZ = getattr(settings, 'ACTIVE_QUIZ', 1)
