#
#  The Ball Game Project
#
#  Copyright (c) 2022 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from django import forms
from django.urls import reverse


class LoginForm(forms.Form):
    username = forms.CharField(label='Username',
                               help_text='Your given username',
                               required=True,
                               min_length=4,
                               max_length=150)
    password = forms.CharField(label='Password',
                               help_text='More than 8 characters',
                               required=True,
                               widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'login-form-id'
        self.helper.form_method = 'post'
        self.helper.form_action = 'login'
        self.helper.add_input(Submit('submit', 'Login'))
        self.helper.add_input(Button('cancel', 'Cancel',
                                     css_class='btn-secondary',
                                     onclick="window.location.href = '{}';".format(reverse('index'))))
