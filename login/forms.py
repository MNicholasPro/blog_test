# -*- coding: utf-8 -*-
from captcha.fields import CaptchaField
from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256,  widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')


class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label='验证码')

class DepartmentModelForm(forms.Form):
    dept_name = forms.CharField(label="部门名称", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入部门！！！'}))

class PublisherModelForm(forms.Form):
    pub_name = forms.CharField(label="出版社名称", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入出版社！！！'}))

class AuthorModelForm(forms.Form):
    author_name = forms.CharField(label="作者名称", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入作者！！！'}))

class BooktypeModelForm(forms.Form):
    book_type = forms.CharField(label="书籍类型", max_length=64, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入书籍类型！！！'}))