from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    context = {
        "rand_word": get_random_string(length=14),
        "acount": request.session['count']
    }
    return render(request, "random_word/index.html", context)

def reset(request):
    if 'count' in request.session:
        request.session['count'] = 0
    else:
        request.session['count'] = 0
    return redirect('/')