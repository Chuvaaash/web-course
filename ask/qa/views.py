from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.core.paginator import Paginator

#from qa.models import Post
from qa.models import Question
from qa.models import Answer

# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse('I am OK')


def main_page(request):
    questions = Question.objects.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    
    paginator = Paginator(questions, limit)
    paginator.base_url = '?page='
    page = paginator.page(page)

    return render(request, 'main_page.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page
    })

def popular(request):
    questions = Question.objects.popular()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)

    paginator = Paginator(questions, limit)
    paginator.base_url = '?page='
    page = paginator.page(page)

    return render(request, 'popular.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page
    })


def question_page(request, question_number):
    try:
        question = Question.objects.get(pk=question_number)
        question_title = question.title
        question_text = question.text

        answers = Answer.objects.filter(question_id=question_number)

    except Question.DoesNotExist:
        raise Http404

    return render(request, 'question_page.html', {
        'title' : question_title,
        'text' : question_text,
        'answers' : answers
    })

#def post_list_all(request):
#    post = Post.objects.filter(is_published=True)
#    limit = request.GET.get('limit', 2)
#    page = request.GET.get('page', 1)
#    paginator = Paginator(post, limit)
#    paginator.base_url = '?page='
#    page = paginator.page(page)
#    
#    posts_this_page = page.object_list
#    posts_with_url = dict()
#    
#    for post in posts_this_page:
#        post_url = post.get_absolute_url()
#        posts_with_url[post] = post_url
#    
#    testnumber = 'five'
#
#    return render(request, 'post_by_tag.html', {
#        'page_number_type': str(type(page.number)),
#        'page_type': str(type(page)),
#        'pag_page_type': str(type(paginator.page_range)),
#        'pag_page_number_type': str(type(paginator.page_range[1])),
#        
#        'testnumber': 'five',
#
#        'posts': page.object_list,
#        'paginator': paginator,
#        'page': page,
#
#        'posts_with_url': posts_with_url
#    })
#
