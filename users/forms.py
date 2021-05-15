#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   forms.py    
@Contact :   thomaslzb@hotmail.com
@License :   (C)Copyright 2020-2022, Zibin Li

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
28/04/2021 09:30   lzb       1.0         None
"""

from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from utils.views import email_check


class LoginForm(forms.Form):
    email = forms.EmailField(required=True, error_messages={"required": _("请输入登录的电子邮件")})
    password = forms.CharField(required=True, min_length=8, error_messages={"required": _("请输入登录密码")})
    captcha = CaptchaField(error_messages={'invalid': _('验证码错误')})


class RegisterForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=20, required=True,
                               error_messages={"required": _("请输入用户名")})
    email = forms.CharField(widget=forms.PasswordInput, required=True ,
                            error_messages={"required": _("请输入登录的电子邮件")})
    password1 = forms.CharField(widget=forms.PasswordInput, required=True, error_messages={"required": _("请输入密码")})
    password2 = forms.CharField(widget=forms.PasswordInput, required=True, error_messages={"required": _("请输入密码")})
    agree_term = forms.BooleanField()

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) < 4:
            raise forms.ValidationError(_("用户名最少需要4个英文字母"))
        elif len(username) > 20:
            raise forms.ValidationError(_("用户名不能太长"))
        else:
            filter_result = User.objects.filter(username__exact=username)
            if len(filter_result) > 0:
                raise forms.ValidationError(_("用户名已经存在"))

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email_check(email):
            filter_result = User.objects.filter(email__exact=email)
            if len(filter_result) > 0:
                raise forms.ValidationError(_("该电子邮件地址已经存在"))
        else:
            raise forms.ValidationError(_("请输入合法的电子邮件地址"))

        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError(_('密码长度不能少于8个字符'))
        elif len(password) > 20:
            raise forms.ValidationError(_("密码长度最大为20个字符"))

        return password

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if password and re_password and password != re_password:
            raise forms.ValidationError(_("两次输入的密码不匹配"))

        return re_password


class ForgetPwdForm(forms.Form):
    username = forms.CharField(max_length=20, required=True, error_messages={"required": _("请输入用户名")})
    email = forms.CharField(required=True, error_messages={"required": _("请输入登录的电子邮件")})
    agree_term = forms.BooleanField()

    def clean(self):
        username = self.data.get('username')
        email = self.data.get('email')

        filter_result = User.objects.filter(username__exact=username, email__exact=email)
        if len(filter_result) == 0:
            raise forms.ValidationError(_("输入的用户或邮件不存在"))

        return

    def clean_agree_term(self):
        agree_term = self.data.get('agree_term')
        return agree_term

