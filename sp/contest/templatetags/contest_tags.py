from django import template
from django.utils.safestring import mark_safe
from django.conf import settings
from sp.contest.models import Work, Contest
from sp.contest import settings as opts

register = template.Library()

@register.simple_tag(takes_context=True)
def get_avatar_url(context, user):
    url = context['STATIC_URL'] + 'i/avatar_nophoto.jpg'
    for sa in user.social_auth.all():
        if sa.provider=='facebook':
            url = 'http://graph.facebook.com/%s/picture' % sa.uid
            break
    return url

@register.inclusion_tag('%s/%s' % (settings.TEMPLATE_THEME, 'contest/templatetags/other_works.html'), takes_context=True)
def other_works(context, contest_id, count):
    contest = Contest.objects.get( id=contest_id )
    works = Work.objects.filter(contest=contest, is_published=True).order_by('-count_votes')[:count]
    return {'contest': contest, 'works': works, 'STATIC_URL': context['STATIC_URL']}
    
@register.simple_tag(takes_context=False)
def count_works(contest_id):
    return Work.objects.filter(contest__id=contest_id, is_published=True).count()

@register.inclusion_tag('%s/%s' % (settings.TEMPLATE_THEME, 'contest/photo_block.html'), takes_context=True)
def photo_block(context, category_id, count):
    contest = Contest.objects.get( id=opts.ACTIVE_CONTEST )
    works = Work.objects.filter(contest=contest, is_published=True, category=category_id)[:count]
    return {'contest': contest, 'works': works, 'STATIC_URL': context['STATIC_URL'], 'user': context['user']}
