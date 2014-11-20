# -*- coding: utf-8 -*-
import json
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, Http404
from django.core.urlresolvers import reverse
from django.conf import settings
from sp.quiz.models import Quiz, Answer, ScoreVariant, UserScore, Question
from sp.quiz import settings as opts


def index(request):
    quiz = get_object_or_404(Quiz, id=opts.ACTIVE_QUIZ)
    return render_to_response('%s/%s' % (settings.TEMPLATE_THEME, 'quiz/index.html'),
                                {
                                    'quiz': quiz,
                                },
                                context_instance=RequestContext(request))


def quiz(request, quiz_id=None):
    quiz = get_object_or_404(Quiz, id=(quiz_id or opts.ACTIVE_QUIZ))
    return render_to_response('%s/%s' % (settings.TEMPLATE_THEME, 'quiz/quiz.html'),
                                {
                                    'quiz': quiz,
                                },
                                context_instance=RequestContext(request))
                                
def set_email(request):
    if request.method == "POST":
        quiz = get_object_or_404(Quiz, id=opts.ACTIVE_QUIZ)
        score = 0
        answers = []
        error = None
        if 'email' in request.POST:
            scores = UserScore.objects.filter(quiz=quiz, email=request.POST['email'])
            if len(scores) == 0:
                return quiz_send(request)
            else:
                error = u'Этот e-mail адрес уже участвует в розыгрыше'
        for param in request.POST:
            if param.startswith('answer_'):
                id = int(param[7:])
                answer = Answer.objects.get(id=id)
                score += answer.score
                answers.append(answer)

        variants = quiz.score_variants.filter(from_score__lte=score, upto_score__gte=score)
        result = None
        if len(variants):
            result = variants[0]

        return render_to_response('%s/%s' % (settings.TEMPLATE_THEME, 'quiz/set_email.html'),
                                {
                                    'quiz': quiz,
                                    'answers': answers,
                                    'result': result,
                                    'error': error,
                                },
                                context_instance=RequestContext(request))
    else:
        return HttpResponseBadRequest()
            
                                
def quiz_send(request):
    if request.method == "POST":
        quiz = get_object_or_404(Quiz, id=opts.ACTIVE_QUIZ)
        score = 0
        answers = []
        for param in request.POST:
            if param.startswith('answer_'):
                id = int(param[7:])
                answer = Answer.objects.get(id=id)
                score += answer.score
                answers.append(answer)

        if not quiz.is_test:            
            userscore = UserScore(quiz=quiz, score=score, finished=True)
            if request.user.is_authenticated():
                scores = UserScore.objects.filter(quiz=quiz, user=request.user)
                if len(scores) == 0:
                    userscore.user = request.user
                    userscore.save()
            elif "email" in request.POST:
                scores = UserScore.objects.filter(quiz=quiz, email=request.POST['email'])
                if len(scores) == 0:
                    userscore.email = request.POST["email"]
                    userscore.save()
            else:
                return HttpResponseBadRequest()

        variants = quiz.score_variants.filter(from_score__lte=score, upto_score__gte=score)
        if len(variants):
            request.session['score'] = score
            return HttpResponseRedirect(reverse('quiz_result', args=[variants[0].id]))
        else:
            if quiz.is_test:
                raise Http404('No such score')
            else:
                return HttpResponseRedirect(reverse('quiz_finish'))
    else:
        return HttpResponseBadRequest()


def quiz_result(request, id):
    score = request.session.get('score') if 'score' in request.session else None
    if 'score' in request.session:
        request.session.pop('score')
    result = get_object_or_404(ScoreVariant, id=id)
    return render_to_response('%s/%s' % (settings.TEMPLATE_THEME, 'quiz/quiz_result.html'),
                                {
                                    'result': result,
                                    'score': score
                                },
                                context_instance=RequestContext(request))


def quiz_finish(request):
    return render_to_response('%s/%s' % (settings.TEMPLATE_THEME, 'quiz/quiz_result.html'),
                                {},
                                context_instance=RequestContext(request))

def get_scores(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return HttpResponse(json.dumps(list(question.answers.values_list('score', flat=True))))