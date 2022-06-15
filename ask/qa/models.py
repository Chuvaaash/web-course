from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
   def new(self):
       return super().get_queryset().order_by('-added_at')

   def popular(self):
       return super().get_queryset().order_by('-likes')

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=True)
    author = models.ForeignKey(User, related_name='question_author', null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='likes_list')
    objects = QuestionManager()


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
