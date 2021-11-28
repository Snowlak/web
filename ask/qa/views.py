from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Question
from django.shortcuts import render


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def post_all_new_question(request):
    posts = Question.objects.new()
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


def post_all_popular_question(request):
    try:
        page = int(request.GET.get('page'))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    posts = Question.objects.popular()
    paginator = Paginator(posts, 10)
    page = paginator.page(page)
    return render(request, 'posts.html', {
        'title': 'Popular',
        'posts': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def one_post(request, pk):
    q = Question.objects.get_object_or_404(pk=pk)
    return render(request, 'post/one_post_page.html', {
        'post': q,
    })
