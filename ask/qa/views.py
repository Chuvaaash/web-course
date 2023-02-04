from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.core.paginator import Paginator

#from qa.models import Post
from qa.models import Question
from qa.models import Answer
#from qa.forms import AddPostForm
#from qa.forms import is_ethic
from qa.forms import AskForm
from qa.forms import AnswerForm

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
        question_url = request.path_info
        if request.method == 'POST':
            answer_form = AnswerForm(request.POST)
            if answer_form.is_valid():
                answer = answer_form.save(question_number)
                return HttpResponseRedirect(question_url)
        else:
            answer_form = AnswerForm()

        question = Question.objects.get(pk=question_number)
        question_title = question.title
        question_text = question.text
    
        answers = Answer.objects.filter(question_id=question_number)

    except Question.DoesNotExist:
        raise Http404

    return render(request, 'question_page.html', {
        'title' : question_title,
        'text' : question_text,
        'answers' : answers,
        'answer_form' : answer_form,
        'question_url' : question_url
    })

#def post_list_all(request):
#    post = Post.objects.filter(is_published=True)
#    limit = request.GET.get('limit', 2)
#    page = request.GET.get('page', 1)
#    paginator = Paginator(post, limit)
#   paginator.base_url = '?page='
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


#def post_page(request, post_number):
#    try:
#        post = Post.objects.get(pk=post_number)
#        post_title = post.title
#        post_content = post.content
#    except Post.DoesNotExist:
#        raise Http404
#    return render(request, 'post_page.html', {
#            'title' : post_title,
#            'content' : post_content
#        })


#def post_add(request):
#    if request.method == "POST":
#        form = AddPostForm(request.POST)
#        if form.is_valid():
#            post = form.save()
#            url = post.get_absolute_url()
#            return HttpResponseRedirect(url)
#    else:
#        form = AddPostForm()
#    return render(request, 'post_add.html', {
#        'form': form
#     })


def create_question(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'create_question.html', {
        'form': form
   })
