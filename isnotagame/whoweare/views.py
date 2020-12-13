from django.shortcuts import render
from django.http import Http404, HttpResponse

# Create your views here.
def index(request):
    return render(request, "whoweare/index.html")

# The texts are much longer in reality, but have
# been shortened here to save space
contents = ["We are a little group trying to make you think more than you usual do.", 
        "We really do not know!!! Maybe it is the right moment to show the world, that in fact, you can do whatever you want to do... You just need commit, focus and sheer will.",
        "Stage 1 : The time is running (tic-toc-tic-toc). You have a multiple choices questions, so pick an answer. Stage 2: Building...",
        "If you want to contribute whit us, first you must to complete our first challenge before 01/01/2021, being at least the tenth best time. Do you want? so you must to show us how good you are... We are waiting for you. Remember you have a unique oportunity to be part of this..."]

def section(request, num):
    if 1 <= num <= 4:
        return HttpResponse(contents[num - 1])
    else:
        raise Http404("What are you looking for?? Is not here... for now....")

def go(request):
    return render(request, "stage1/index.html")