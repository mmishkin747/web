from django import forms
from .models import Question, Answer
from django.shortcuts import get_object_or_404


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_date['title']
        if title.strip() == '':
            raise forms.ValidationError(
                'Title is empty', code='validation_error')
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if text.strip() == '':
            raise forms.ValidationError(
                'Text is empty', code='validation_error')
        return text

    def save(self):
        if self._user.is_anonymous():
            self.cleaned_data['author_id'] = 1
        else:
            self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_text(self):
        text = self.cleaned_data['text']
        if text.strip() == '':
            raise forms.ValidationError(
                'Text is empty', code='validation_error')
        return text

    def cleaned_data(self):
        try:
            question = int(self.cleaned_data['question'])
        except ValueError:
            raise forms.ValidationError(
                'Invalid date', code='validation_error')
        return question

    def save(self):
        self.cleaned_data['question'] = get_object_or_404(
            Question, pk=self.cleaned_data['question'])

        if self._user.is_anonymous():
            self.cleaned_data['author_id'] = 1
        else:
            self.cleaned_data['author'] = self._user

        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
