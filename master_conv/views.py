from django.shortcuts import render
from . import forms
from . import models
# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            name = register_form.cleaned_data.get('name')
            phone = register_form.cleaned_data.get('phone')
            sex = register_form.cleaned_data.get('sex')
            fru_name = register_form.cleaned_data.get('fru_name')
            path_home = register_form.cleaned_data.get('path_home')
            if request.method == 'POST':
                new_user = models.User_goods_customer()
                new_user.name = name
                new_user.phone = phone
                new_user.sex = sex
                new_user.fru_name = fru_name
                new_user.path_home = path_home
                new_user.save()
    register_form = forms.RegisterForm()
    return render(request, 'register.html', locals())