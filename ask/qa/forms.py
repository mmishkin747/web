from django import forms
from .models import Question, Answer
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        question = Question(**self.cleaned_data)
        question.author = self._user
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def save(self):
        self.cleaned_data['question'] = get_object_or_404(
            Question, pk=self.cleaned_data['question'])
        answer = Answer(**self.cleaned_data)
        answer.author = self._user
        answer.save()
        return answer


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if username.strip() == '':
    #         raise forms.ValidationError('Username is empty',
    #                                     code='validation_error')
    #     return username
    #
    # def clean_password(self):
    #     password = self.cleaned_data['password']
    #     if password.strip() == '':
    #         raise forms.ValidationError('Password is empty',
    #                                     code='validation_error')
    #     return password

    def save(self):
        auth = authenticate(**self.cleaned_data)
        return auth
