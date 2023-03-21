#
#  The Ball Game Project
#
#  Copyright (c) 2021-23 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.urls import reverse


class RegistrationForm(forms.Form):

    username = forms.CharField(label='Username', min_length=4, max_length=150)
    email = forms.EmailField(label='e-Mail')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'registration-id'
        self.helper.form_method = 'post'
        self.helper.form_action = '/register/'
        self.helper.add_input(Submit('submit', 'Register'))
        self.helper.add_input(Button('cancel', 'Cancel',
                                     css_class='btn-secondary',
                                     onclick="window.location.href = '{}';".format(reverse('index'))))

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

