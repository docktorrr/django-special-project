# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class AuthenticationForm(forms.Form):

    email = forms.EmailField(label=u"E-mail", max_length=50)
    password = forms.CharField(label=u"Пароль", widget=forms.PasswordInput)

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(AuthenticationForm, self).__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            self.user_cache = authenticate(email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(u"Неверный логин или пароль")
            elif not self.user_cache.is_active:
                raise forms.ValidationError(u"Аккаунт не активирован")

        return self.cleaned_data

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache


class RegistrationForm(forms.Form):

    email = forms.EmailField(label=u"E-mail", max_length=50)
    password = forms.CharField(label=u"Пароль", widget=forms.PasswordInput)
    password1 = forms.CharField(label=u"Подтверждение пароля", widget=forms.PasswordInput)
    first_name = forms.CharField(label=u"Имя", max_length=150)
    avatar = forms.ImageField(label=u"Aватар")

    def clean_password1(self):
        pass1 = self.cleaned_data.get('password', '')
        pass2 = self.cleaned_data['password1']
        if pass2 == '':
            raise forms.ValidationError(["Пароль не введен"])
        if pass1 != pass2:
            raise forms.ValidationError(["Пароли не совпадают"])
        return pass2

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError([u"Пользователем с таким адресом уже существует"])
        return email

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar', False)
        if avatar:
            if avatar._size > 1*1024*1024:
                raise forms.ValidationError(u"Изображение слишком большое (>1mb)")
        else:
            if self.fields['avatar'].required:
                raise forms.ValidationError("Couldn't read uploaded image")
        return avatar

    def save(self):
        user = User.objects.create_user(
            username = self.cleaned_data['email'],
            email = self.cleaned_data['email'],
            password = self.cleaned_data['password'],
        )
        user.first_name = self.cleaned_data['first_name']
        user.is_active = True
        user.save()
        return user
