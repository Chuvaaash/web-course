from django import forms

#from qa.models import Post
from qa.models import Question
from qa.models import Answer
from qa.models import User

#def is_ethic(message):
#    if message == 'loh':
#        return False
#    else:
#        return True


#class AddPostForm(forms.Form):
#    title = forms.CharField(max_length=100)
#    content = forms.CharField(widget=forms.Textarea)
#
#    def clean_message(self):
#        if not is_ethic(message):
#            raise forms.ValidationError(u'Sam ty loh', code=12)
#
#        return message + '\nThank you for your attention.'

#    def save(self):
#        post = Post(**self.cleaned_data, is_published=True)
#        post.save()
#        return post


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def save(self, user_id):
        question = Question(**self.cleaned_data, author_id=user_id)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.ModelChoiceField(queryset=Question.objects.all(), empty_label ='select', to_field_name ='title')
#    user = forms.ModelChoiceField(queryset=User.objects.all())

    def save(self, question_number, user_id):
        answer = Answer(text=self.cleaned_data['text'], question_id=question_number, author_id=user_id)
        answer.save()
        return answer


class UserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        return user


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
