#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   email_send.py.py    
@Contact :   thomaslzb@hotmail.com
@License :   (C)Copyright 2020-2022, Zibin Li

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
11/05/2021 11:47   lzb       1.0         None
"""

from random import Random
from django.core.mail import send_mail
from django.contrib.auth.models import User

from users.models import EmailVerifyRecord
from dianda.settings import EMAIL_FROM, IS_SEND_MAIL


def get_random_string(random_length=8):
    random_string = ""
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        random_string += chars[random.randint(0, length)]
    return random_string


def send_register_email(e_mail, send_type="register", ):
    user_id = User.objects.filter(email__exact=e_mail)[0].id

    random_code = str(user_id) + '=' + get_random_string(20)

    email_record = EmailVerifyRecord()
    email_record.email = e_mail
    email_record.code = random_code
    email_record.send_type = send_type
    email_record.is_used = 0
    email_record.save()

    if IS_SEND_MAIL:
        if send_type == "register":
            email_title = "注册成功，激活账号"
            email_body = "点击这里激活账号， http://127.0.0.1:8000/active/{0}".format(random_code)
            email_body += "\n\r"
            email_body += "点达公司"
            send_status = send_mail(email_title, email_body, EMAIL_FROM, [e_mail])
            if send_status:
                pass
        elif send_type == "forget":
            email_title = "找回密码"
            email_body = "点击这里，找回密码 http://127.0.0.1:8000/password_reset/{0}".format(random_code)
            email_body += "\n\r"
            email_body += "点达公司"
            send_status = send_mail(email_title, email_body, EMAIL_FROM, [e_mail])
            if send_status:
                pass
