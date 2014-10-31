from django import template
from django.utils.safestring import mark_safe
from django.db.models import Sum
from django.contrib.auth.models import User

register = template.Library()

@register.inclusion_tag('users/templatetags/user_card.html', takes_context=True)
def user_card(context):
    from contest.models import Work
    user = context['user']
    rating1 = Work.objects.filter(contest__id=1, user=user).aggregate(rating=Sum('count_votes'))['rating'] or 0
    rating2 = Work.objects.filter(contest__id=2, user=user).aggregate(rating=Sum('count_votes'))['rating'] or 0
    rating3 = Work.objects.filter(contest__id=3, user=user).aggregate(rating=Sum('count_votes'))['rating'] or 0
    sum = rating1 + rating2 + rating3
    return {
            'STATIC_URL': context['STATIC_URL'], 
            'user': user, 
            'rating1': rating1, 
            'rating2': rating2,
            'rating3': rating3,
            'sum': sum,
            }

@register.inclusion_tag('users/templatetags/rating_item.html', takes_context=True)
def rating_item(context, user_id, place=0):
    from contest.models import Work    
    user = User.objects.get(id=user_id)
    rating1 = Work.objects.filter(contest__id=1, user=user).aggregate(rating=Sum('count_votes'))['rating'] or 0
    rating2 = Work.objects.filter(contest__id=2, user=user).aggregate(rating=Sum('count_votes'))['rating'] or 0
    rating3 = Work.objects.filter(contest__id=3, user=user).aggregate(rating=Sum('count_votes'))['rating'] or 0
    sum = rating1 + rating2 + rating3
    return {
            'STATIC_URL': context['STATIC_URL'], 
            'user': user, 
            'rating1': rating1, 
            'rating2': rating2,
            'rating3': rating3,
            'sum': sum,
            'place': place,
            }
            