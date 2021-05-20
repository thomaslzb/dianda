#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.utils.translation import gettext as _

from users.forms import LoginForm, RegisterForm, ForgetPwdForm
from users.models import UserProfile
from utils.email_send import send_register_email
from utils.tools import validate_mobile


def index(request):
    return render(request, 'main_menu.html')


# 用户登录
class LoginView(View):
    def get(self, request):
        hash_key = CaptchaStore.generate_key()
        image_url = captcha_image_url(hash_key)
        msg = ''
        login_form = LoginForm()
        return render(request, "login.html", locals())

    def post(self, request):
        login_form = LoginForm(request.POST)
        email = request.POST.get("email", "")
        pass_word = request.POST.get("password", "")
        if login_form.is_valid():
            filter_result = User.objects.filter(email__exact=email)
            username = filter_result[0].username
            user = authenticate(username=username, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "login_success.html", locals())
                else:
                    hash_key = CaptchaStore.generate_key()
                    image_url = captcha_image_url(hash_key)
                    msg = _("用户被暂停，请联系系统管理员")
                    return render(request, "login.html", locals())
            else:
                # 图片验证码
                # hashkey验证码生成的秘钥，image_url验证码的图片地址
                hash_key = CaptchaStore.generate_key()
                image_url = captcha_image_url(hash_key)
                msg = _("用户名或者密码错误")
                return render(request, "login.html", locals())
        else:
            hash_key = CaptchaStore.generate_key()
            image_url = captcha_image_url(hash_key)
            msg = _("验证码错误")
            # Python内置了一个locals()函数，它返回当前所有的本地变量字典
            return render(request, "login.html", locals())


# 用户注册(包括手机注册，邮箱注册)
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {"register_form": register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            pass_word = request.POST.get("password", "")

            if UserProfile.objects.filter(email=user_name):
                return render(request, "register.html", {"register_form": register_form, "msg": "email is existed"})

            send_register_email(user_name, "register",)

            return render(request, "register_mail_success.html")
        else:
            return render(request, "register.html", {"register_form": register_form})


# 忘记密码
class ForgotPwdView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "forgot_password.html", {"register_form": register_form})

    def post(self, request):
        forget_pwd_form = ForgetPwdForm(request.POST)

        if forget_pwd_form.is_valid():
            user_id = request.POST.get("user_id", "")
            if validate_mobile(user_id):
                # send a new mail for reset password 测试成功
                # send_register_mobile(user_id, "forget", )
                pass
                return redirect('users:login')
            else:
                # send a new mail for reset password 测试成功
                send_register_email(user_id, "forget",)
                # 提示已经发了邮件
                return render(request, "send_resetPwd_success.html")
        else:
            return render(request, "forgot_password.html", {"forgetPwd_form": forget_pwd_form})


