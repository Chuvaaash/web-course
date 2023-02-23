"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path

#urlpatterns = [
#    path('admin/', admin.site.urls),
#]

from qa import views

urlpatterns = [
#        path('', views.test),
        path('login/', views.login_page),
        path('question/<question_number>/', views.question_page),
        path('ask/', views.create_question),
        path('popular/', views.popular),
        path('', views.main_page),
        path('signup/', views.signup)
#        path('new/', views.post_list_all),
#        path('create/', views.post_add),
#        path('create_post/', views.post_add),
#        path('post/<post_number>/', views.post_page),
    ]
