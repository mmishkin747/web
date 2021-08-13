from django import forms
from .models import Question, Answer
from django.shortcuts import get_object_or_404


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)


#    def clean_title(self):
#        title = self.cleaned_date['title']
#        if title.strip() == '':
#            raise forms.ValidationError(
#                'Title is empty', code='validation_error')
#        return title

#    def clean_text(self):
#        text = self.cleaned_data['text']
#        if text.strip() == '':
#            raise forms.ValidationError(
#                'Text is empty', code='validation_error')
#        return text


    def save(self):
        question = Question(**self.cleaned_data)
        question.author = self._user
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    # def clean_text(self):
    #     text = self.cleaned_data['text']
    #     if text.strip() == '':
    #         raise forms.ValidationError(
    #             'Text is empty', code='validation_error')
    #     return text
    #
    # def cleaned_data(self):
    #     try:
    #         question = int(self.cleaned_data['question'])
    #     except ValueError:
    #         raise forms.ValidationError(
    #             'Invalid date', code='validation_error')
    #     return question

    def save(self):
        self.cleaned_data['question'] = get_object_or_404(
            Question, pk=self.cleaned_data['question'])
        answer = Answer(**self.cleaned_data)
        answer.author = self._user
        answer.save()
        return answer
