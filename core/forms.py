# coding=utf-8
from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

from core.models import User

ERROR_REQUIRED = u'Обязательное поле'
ERROR_MAX_LENGTH = u'Слишком длинное поле'
ERROR_MIN_LENGTH = u'Пароль должен быть длиннее 8 символов'

DEFAULT_ERRORS = {'required': ERROR_REQUIRED, 'max_length': ERROR_MAX_LENGTH, 'min_length': ERROR_MIN_LENGTH}


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(initial='', min_length=8, max_length=50, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    check_password = forms.CharField(initial='', min_length=8, max_length=50, required=True,
                                     widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].required = False
        for field in self.fields:
            self.fields[field].error_messages = DEFAULT_ERRORS
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = self.cleaned_data.get('password')
        check_password = self.cleaned_data.pop('check_password', None)
        if password != check_password:
            self.add_error('password', u'Пароли должны совпадать')
            raise ValidationError('Passwords do not match')
        return cleaned_data

    def save(self, commit=True):
        user = User.objects.create_user(
            email=self.cleaned_data.pop('email'),
            password=self.cleaned_data.pop('password'),
            **self.cleaned_data)
        return user


class LoginForm(forms.ModelForm):
    password = forms.CharField(initial='', max_length=50, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].error_messages = DEFAULT_ERRORS
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            self.cleaned_data['user'] = user
        else:
            self.add_error('email', 'Неправильный логин или пароль')
            raise ValidationError('Unable to login')
        return self.cleaned_data
