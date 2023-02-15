from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    name = "Bob"
    context = {'name': name}
    return render(request, 'travel/home.html', context)
