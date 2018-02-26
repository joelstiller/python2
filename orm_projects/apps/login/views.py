# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Login
from django.contrib.messages import error
from django.shortcuts import render, HttpResponse, redirect
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def success(request):
    return render(request, "login/success.html")

def register(request):
    errors = Login.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/')

    # Hashing password like a good boy
    hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    Login.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=hashed_password
    )
    return redirect('/')

def login(request):
    user = Login.objects.filter(email=request.POST['email'])
    if not user:
        message = "Your account was not found."
        error(request, message, extra_tags='email')
        return redirect('/')
    else:
        password = request.POST['password']
        if bcrypt.checkpw(password.encode(), user[0].password.encode()):
            request.session['first_name'] = user[0].first_name
            return redirect('/success')
        else:
            message = "Incorrect Password"
            error(request, message, extra_tags='password')
            return redirect('/')

def logout(request):
    request.session.delete()
    return redirect('/')