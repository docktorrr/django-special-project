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
    if 'time' in dict:
        recipes = recipes.filter(cooking_time=dict['time'])
    
    return render_to_response('%s/%s' % (settings.TEMPLATE_THEME, 'publications/recipes.html'), {'recipes': recipes, 'params': dict}, context_instance=RequestContext(request))
