#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   tools.py    
@Contact :   thomaslzb@hotmail.com
@License :   (C)Copyright 2020-2022, Zibin Li

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
12/10/2020 13:48   lzb       1.0         None
"""
import re
import time


def exchange_string(s):
    """
    将字符串中的空格，转换成为下划线
    """
    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)

    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '-', s)

    return s


def is_float(num_str):
    """
     判断字符串是否是浮点数(整数算小数)
    :param num_str: 字符串
    :return: True / False
    """
    num_str = str(num_str).strip().lstrip('-').lstrip('+')  # 去除正数(+)、负数(-)符号
    try:
        num_str = float(num_str)
        return True
    except:
        return False


def format_postcode(postcode):
    """
    格式化英国邮编
    :param postcode: 正常的英国邮编
    :return: 去掉后面三位后，邮编字符串
    """
    postcode = postcode.strip().upper()
    if len(postcode) > 3:
        postcode = postcode[0:len(postcode) - 3].strip() + \
                   " " + postcode[len(postcode) - 3:len(postcode)]
    return postcode


def run_timer(func):
    """
    统计某函数运行多长时间的装饰器
    :param func: 函数体
    :return:
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        ret_value = func(*args, **kwargs)
        end = time.time()
        used = end - start
        print(f'{func.__name__} used {used}')
        return ret_value
    return wrapper


def validate_email(email):
    """
    判断是否是合法的email地址
    :param email: email 字符串
    :return: True / False
    """
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) is not None:
            return True
    return False


def validate_mobile(phone):
    """
    判断是否是合法的手机号码
    :param phone: 手机号码
    :return: True / False
    """
    if len(phone) == 11 and re.match(r'1\d{10}', phone):
        return True
    return False
