#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   urls.py    
@Contact :   thomaslzb@hotmail.com
@License :   (C)Copyright 2020-2022, Zibin Li

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
27/04/2021 18:37   lzb       1.0         None
"""

from django.urls import path

from . import views
from .views import RegisterView, LoginView, ForgotPwdView

app_name = 'users'

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('forgot-pwd', ForgotPwdView.as_view(), name='forgot_pwd'),

]
