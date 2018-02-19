from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request, "surveys/index.html")

def result(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['lang']
    request.session['comment'] = request.POST['comment'] 
    return render(request, "surveys/result.html")