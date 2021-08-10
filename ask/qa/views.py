from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Answer
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

def test(request, *args, **kwargs):
    return HttpResponse('OK')


def index(request):
    try:
        page = int(request.GET.get('page'))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    questions = Question.objects.new()
    paginator = Paginator(questions, 10)
    page = paginator.page(page)
    context = {
        'title': 'LaTest',
        'paginator': paginator,
        'questions':page.object_list,
        'page': page,
        'user': request.user,
        'session': request.session,
    }
    return render(request, 'qa/index.html', context)


def popular(request):
    try:
        page = int(request.GET.get('page'))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    questions = Question.objects.popular()
    paginator = Paginator(questions, 10)
    page = paginator.page(page)
    context = {
        'title': 'Popular',
        'paginator': paginator,
        'questions':page.object_list,
        'page': page,
        'user': request.user,
        'session': request.session,
    }
    return render(request, 'qa/popular.html', context)

def question(request, question_id):
    q = get_object_or_404(Question, id=question_id)
    a = Answer.objects.filter(question=question_id).order_by('-added_at')
    context = {
        'question':q,
        'answer': a,
    }
    return render(request, 'qa/question.html', context)
