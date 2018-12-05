import time

import hashlib
import random
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from app.models import User


def index(request):
    return render(request, 'mainWeb.html')

# 自定义token规则
def generate_token():
    token = str(time.time()) + str(random.random());
    md5 = hashlib.md5();
    md5.update(token.encode('utf-8'));
    return md5.hexdigest();

def generate_pwd(pwd):
    md5 = hashlib.md5();
    md5.update(pwd.encode('utf-8'));
    return md5.hexdigest();

def login(request):
    if request.method == 'GET':
        # return HttpResponse(request.session.get('sessionid'));
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username');
        pwd = request.POST.get('pwd');
        user = User.objects.filter(username=username).filter(pwd=pwd);
        if user.count():
            response = redirect('app:index');
            user_ = user.first();
            user_.token =  generate_token();
            user_.save();
            request.session['token'] = user_.token;
            request.session.set_expiry(60 * 2)
            # request.session['username'] = username;
            # request.session['pwd'] = pwd;
            return response
        else:
            return render(request, 'login.html', context={'err': '用户名或密码错误'});


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username');
        pwd = request.POST.get('pwd');
        user = User();
        user.username = username;
        # 密码md5加密
        user.pwd = generate_pwd(pwd);
        user.token = generate_token();
        user.save();
        response = redirect('app:login');
        request.session['token'] = user.token;
        request.session.set_expiry(60 * 2);
        return response


def cart(request):
    return render(request, 'cart.html')


def index_(request):
    return render(request, 'login.html')
