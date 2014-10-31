# -*- coding: utf-8 -*-
from django import forms
from sp.qa.models import Question


class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Question
        fields = ['name', 'email', 'text']