"""
@File : forms.py
@copyright : GG
@Coder: Leslie_s
@Date: 2020/2/6
"""
from django import forms
from master_conv import models
class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    name = forms.CharField(label="客户姓名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.IntegerField(label="收货电话",widget=forms.NumberInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    fru_name = forms.CharField(label="菜名", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    path_home = forms.CharField(label="收货地址", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))