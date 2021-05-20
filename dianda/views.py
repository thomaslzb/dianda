#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   views.py    
@Contact :   thomaslzb@hotmail.com
@License :   (C)Copyright 2020-2022, Zibin Li

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
11/05/2021 11:39   lzb       1.0         None
"""


from django.http import HttpResponse
from django.shortcuts import render


def ptp_home(request):
    return render(request, 'building.html')


def bad_request(request, template_name='errors/page_404.html'):   # 400
    return render(request, template_name, status=400)


def permission_denied(request, template_name='errors/page_403.html'):  # 403 - ok
    return render(request, template_name, status=403)


def page_not_found(request, template_name='errors/page_404.html'):  # 404 - ok
    return render(request, template_name, status=404)


def server_error(request, template_name='errors/page_500.html'):  # 500 - ok
    return render(request, template_name, status=500)


