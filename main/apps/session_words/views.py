from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime

def index(request):
    return render(request, 'session_words/index.html')

def process(request, methods="POST"):
    if "word_list" not in request.session:
        request.session["word_list"] = []
    class_str = ""
    
    if "big" in request.POST:
        class_str += "big_"

    if request.POST["color"] == "red":
        class_str += "red"
    elif request.POST["color"] == "green":
        class_str += "green"
    elif request.POST["color"] == "blue":
        class_str += "blue"

    new_word = {
        "word": request.POST["user_input"],
        "class": class_str,
        "time": strftime("%H:%M, %b %d, %Y", localtime())
    }

    new_list = request.session["word_list"] 
    new_list.append(new_word)
    request.session["word_list"] = new_list
    return redirect('/')

def clear(request):
    if "word_list" in request.session:
        del request.session["word_list"]
    return redirect('/')