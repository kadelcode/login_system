from cProfile import label
import re
from django import forms
from django.forms import formset_factory
import datetime

class ContactForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'field-required'

    subject = forms.CharField(max_length=100, label='Subject of Message', help_text='Max length of 200',required=False)
    message = forms.CharField(widget=forms.Textarea, initial='What will you need help on?', min_length=20)
    sender = forms.EmailField(help_text='Enter a valid email')
    cc_myself = forms.BooleanField(required=True)
    country = forms.ChoiceField(choices=[
        ('ENG', 'England'),
        ('US', 'USA'),
        ('NIG', 'Nigeria'),
    ])

    floatfield = forms.FloatField(min_value=1, max_value=5)
    ip_address = forms.GenericIPAddressField()
    json_field = forms.JSONField()
    multiple_choice = forms.MultipleChoiceField(choices=[
        ('ENG', 'England'),
        ('US', 'USA'),
        ('NIG', 'Nigeria'),
        ('ENG', 'England'),
        ('US', 'USA'),
        ('NIG', 'Nigeria'),
        ('ENG', 'England'),
        ('US', 'USA'),
        ('NIG', 'Nigeria'),
        ])

    nullbool = forms.NullBooleanField()