from django.shortcuts import render
from django.http import Http404, HttpResponse

# Create your views here.
def index(request):
    return render(request, "whoweare/index.html")

# The texts are much longer in reality, but have
# been shortened here to save space
texts = ["We are a little group trying to make you think more than you usual do.", 
        "Text 2",
        "Well: Stage 1 : You have a multiple choices questions, so pick an answer, the time is running. Stage 2: Building..."]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")