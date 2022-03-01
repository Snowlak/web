from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Question, Answer
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET
from django.shortcuts import get_object_or_404
from .forms import AnswerForm, AskForm, LoginForm, SignupForm
from django.contrib.auth import authenticate, login


def test(request, *args, **kwargs):
    return HttpResponse('OK')


@require_GET
def post_all(request):
    posts = Question.objects.all()
    try:
        page = int(request.GET.get('page'))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    paginator = Paginator(posts, 10)
    page = paginator.page(page)
    return render(request, 'posts.html', {
        'title': 'Home',
        'posts': page.object_list,
        'paginator': paginator,
        'page': page,
    })


@require_GET
def post_all_new_question(request):
    posts = Question.objects.order_by('-id')
    try:
        page = int(request.GET.get('page'))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    paginator = Paginator(posts, 10)
    page = paginator.page(page)
    return render(request, 'posts.html', {
        'title': 'New posts',
        'posts': page.object_list,
        'paginator': paginator,
        'page': page,
    })


@require_GET
def post_all_popular_question(request):
    try:
        page = int(request.GET.get('page'))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    posts = Question.objects.order_by('-rating')
    paginator = Paginator(posts, 10)
    page = paginator.page(page)
    return render(request, 'posts.html', {
        'title': 'Popular',
        'posts': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def one_post(request, id):
    q = get_object_or_404(Question, pk=id)
    answers = Answer.objects.filter(question_id__exact=int(id))
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            form.save()
            return redirect('/question/{}'.format(id))
        else:
            return render(request, 'post/one_post_page.html', {
                'post': q,
                'answer': answers,
                'form': form,
            })
    else:
        form = AnswerForm(initial={'question': q.id})
        return render(request, 'post/one_post_page.html', {
                'post': q,
                'answer': answers,
                'form': form,
                'likes': q.total_like(),
            })


def add_answer(request, question_id):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            answer.author = request.user
            answer.save()
        return HttpResponseRedirect('/question/{}'.format(question_id))
    else:
        form = AnswerForm(initial={'question': question_id})
    return render(request, 'answer.html', {'form': form})


def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            post = form.save()
            # url = post.get_url()
            return HttpResponseRedirect('/')
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            print(type(user))
            if user is not None:
                if user.is_active:
                    login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form, 'user': request.user})
