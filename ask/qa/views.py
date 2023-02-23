from datetime import datetime, timedelta

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login

#from qa.models import Post
from qa.models import Question
from qa.models import Answer
from qa.models import User
from qa.models import Session
#from qa.forms import AddPostForm
#from qa.forms import is_ethic
from qa.forms import AskForm
from qa.forms import AnswerForm
from qa.forms import UserForm
from qa.forms import LoginForm

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
            if request.user.is_authenticated:
                answer_form = AnswerForm(request.POST)
#                answer_form.user = request.user.id
                if answer_form.is_valid():
                    user_id = request.user.id
                    answer = answer_form.save(question_number, user_id)
                    return HttpResponseRedirect(question_url)
#                else:
#                    return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/signup')
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
        user = request.user
        if user.is_authenticated:
            form = AskForm(request.POST)
            if form.is_valid():
                question = form.save(user.id)
                url = question.get_absolute_url()
                return HttpResponseRedirect(url)
        else:
            return HttpResponseRedirect('/signup')
    else:
        form = AskForm()
    return render(request, 'create_question.html', {
        'form': form
   })

def signup(request):
    if request.method == 'POST':
#        username = request.POST.get('username')
#        email = request.POST.get('email')
#        password = request.POST.get('password')
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            url = '/'
            return HttpResponseRedirect(url)
    else:
        form = UserForm()
    return render(request, 'signup.html', {
        'form': form
    })


#def do_login(user):
#    session = Session()
#    session.sessionid = session.generate_sessionid(session.id)
#    session.user = user
#    session.expires = datetime.now() + timedelta(days=5)
#    session.save()
#    return session.sessionid


#def login(request):
#    if request.method == 'POST':
#        username = request.POST.get('username')
#        password = request.POST.get('password')
#        user = authenticate(username=username, password=password)
#        if user is not None:
#            sessionid = do_login(user)
#            url = '/'
#            response = HttpResponseRedirect(url)
#            response.set_cookie('session', sessionid,
#                    domain = '/', httponly=True,
#                    expires = datetime.now() + timedelta(days=5)
#            )
#            return response
#        else:
#            form = LoginForm()
#            form.username = username
#            form.password = password
#            error = 'Wrong login or password. Try again'
#        return render(request, 'login.html', {
#            'form': form,
#            'error' : error
#        })
#    else:
#        form = LoginForm()
#    return render(request, 'login.html', {
#        'form': form
#    })


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            url = '/'
            response = HttpResponseRedirect(url)
            #set cookie
            return response
        else:
            form = LoginForm()
            error = u'Wrong login or password. Try again'
            return render(request, 'login.html', {
                'form': form,
                'error': error
            })
    else:
        form = LoginForm()
    return render(request, 'login.html', {
        'form': form
    })

