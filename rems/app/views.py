from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def header(request):
    return render(request, 'header.html')


def footer(request):
    return render(request, 'footer.html')


def homepage(request):
    return render(request, 'index.html')
