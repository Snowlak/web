from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Question, Answer
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from .forms import AnswerForm, AskForm


def test(request, *args, **kwargs):
    return HttpResponse('OK')


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


@require_GET
def one_post(request, id):
    q = get_object_or_404(Question, pk=id)
    answers = Answer.objects.filter(question_id__exact=int(id))
    return render(request, 'post/one_post_page.html', {
        'post': q,
        'answer': answers,
    })


@require_POST
def answer(request):
    form = AnswerForm(request.POST)
    if form.is_valid():
        answer = form.save(commit=False)
        answer.author = request.user
        answer.save()
        return redirect(answer.question)


def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect(question)
    else:
        form = AskForm()
    return render(request, 'templates/ask.html', {'form': form})

