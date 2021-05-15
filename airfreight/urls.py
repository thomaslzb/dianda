#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   urls.py    
@Contact :   thomaslzb@hotmail.com
@License :   (C)Copyright 2020-2022, Zibin Li

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
12/05/2021 14:23   lzb       1.0         None
"""
from django.contrib.auth.decorators import login_required
from django.urls import path

from airfreight.views import AirfreightInquireView

app_name = 'airfreight'

urlpatterns = [
    path('inquire/', AirfreightInquireView.as_view(), name='airfreight_inquire'),

]

