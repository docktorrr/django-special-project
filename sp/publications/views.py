# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.conf import settings
from sp.publications.models import Article, Recipe, Tag


def article(request, id):
    article = get_object_or_404(Article, id=id)
    return render_to_response('%s/%s' % (settings.TEMPLATE_THEME, 'publications/article.html'), {'article': article}, context_instance=RequestContext(request))

def recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render_to_response('%s/%s' % (settings.TEMPLATE_THEME, 'publications/recipe.html'), {'recipe': recipe}, context_instance=RequestContext(request))
    
def recipes(request):
    if request.method == 'POST':
        dict = request.POST
    else:
        dict = request.GET
    recipes = Recipe.objects.all()
    if 'tag' in dict:
        try:
            tag = Tag.objects.get(name=dict['tag'])
            recipes = recipes.filter(tags=tag)
        except Tag.DoesNotExist:
            recipes = recipes.none()
    if 'calories' in dict:
        recipes = recipes.filter(calories=dict['calories'])
    if 'time_min' in dict and dict['time_min'] != '':
        recipes = recipes.filter(cooking_time__gte=dict['time_min'])
    if 'time_max' in dict and dict['time_max'] != '':
        recipes = recipes.filter(cooking_time__lte=dict['time_max'])
    
    return render_to_response('%s/%s' % (settings.TEMPLATE_THEME, 'publications/recipes.html'), {'recipes': recipes}, context_instance=RequestContext(request))