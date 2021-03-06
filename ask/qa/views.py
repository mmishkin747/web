from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Answer
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AnswerForm, AskForm, LoginForm, SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def index(request):
    try:
        page = int(request.GET.get('page'))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    questions = Question.objects.all().order_by('-id')
    paginator = Paginator(questions, 10)
    page = paginator.page(page)
    context = {
        'title': 'LaTest',
        'paginator': paginator,
        'questions': page.object_list,
        'page': page,
        'user': request.user,
        'session': request.session,
    }
    return render(request, 'qa/index2.html', context)


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
        'questions': page.object_list,
        'page': page,
        'user': request.user,
        'session': request.session,
    }
    return render(request, 'qa/popular.html', context)


def question(request, question_id):
    q = get_object_or_404(Question, id=question_id)
    a = q.answer_set.all()
    form = AnswerForm(initial={'question': question_id})
    context = {
        'question': q,
        'answer': a,
        'form': form,
    }
    return render(request, 'qa/question.html', context)


def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {'form': form})


def answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            print('Answer is valid')
            form._user = request.user  # User.objects.get(id=1)
            answer = form.save()
            url = answer.get_url()
            print('>>>>>>>>' + url+'<<<<<<<')
            return HttpResponseRedirect(url)
    return HttpResponseRedirect('/')


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            print('no valid')
    form = SignupForm()
    return render(request, 'qa/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    form = LoginForm()
    return render(request, 'qa/login.html', {'form': form})


def user_logout(request):
    if request.user is not None:
        logout(request)
        return HttpResponseRedirect(reverse('index'))
