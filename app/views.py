from django.shortcuts import render
from .forms import *

def index(req):
    name = ''
    captcha = ''
    form = MyForm
    if req.POST:
        form = MyForm(req.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            captcha = form.cleaned_data['captcha']
            print(form.cleaned_data)
    return render(req, 'index.html', context={'form': form, 'name': name, 'captcha': captcha})

