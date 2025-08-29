from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello(request):
    return render(request, "hello.html", {"name": "Sabir"})
    # return HttpResponse("Hello World!")
