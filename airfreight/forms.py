#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   forms.py.py    
@Contact :   thomaslzb@hotmail.com
@License :   (C)Copyright 2020-2022, Zibin Li

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
17/05/2021 08:24   lzb       1.0         空运部分的forms
"""
from django import forms


class AirFreightForm(forms.Form):
    fab_code = forms.CharField(required=False)
    postcode = forms.CharField(required=False)
    hs_code_number = forms.IntegerField(required=True, )
    volume = forms.DecimalField(required=True)
    weight = forms.DecimalField(required=True)

    def clean_hs_code_number(self):
        hs_code_number = int(self.cleaned_data.get('hs_code_number'))
        if hs_code_number <= 0:
            raise forms.ValidationError('HS Code 的数量必须大于0.')
        return hs_code_number

    def clean_volume(self):
        volume = float(self.cleaned_data.get('volume'))
        if volume <= 0:
            raise forms.ValidationError('输入的体积数量必须大于0.')
        return volume

    def clean_weight(self):
        weight = float(self.cleaned_data.get('weight'))
        if weight <= 0:
            raise forms.ValidationError('输入的重量数量必须大于0.')
        return weight
