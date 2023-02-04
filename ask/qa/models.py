from django.db import models
from django.contrib.auth.models import User
from django import forms

class QuestionManager(models.Manager):
   def new(self):
       return super().get_queryset().order_by('-id')

   def popular(self):
       return super().get_queryset().order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=True)
    author = models.ForeignKey(User, related_name='question_author', null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='likes_list')
    objects = QuestionManager()
    
    def get_absolute_url(self):
        return '/question/%d' %self.pk


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

#class Post(models.Model):
#    title = models.CharField(max_length=255)
#    content = models.TextField()
#    creation_date = models.DateTimeField(blank=True, auto_now_add=True)
#    is_published = models.BooleanField(blank=True)
#    def __unicode__(self):
#        return self.title
#    def get_absolute_url(self):
#        return '/post/%d' %self.pk
#    class Meta:
#        db_table = 'blogposts'
#        ordering = ['-creation_date']
#
#
#def is_ethic(message):
#    if not message == 'loh':
#        return True
#    else:
#        return False

