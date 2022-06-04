from django.shortcuts import render, redirect
from .models import Reducer


def home(request):
    return render(request, './reducer/home.html')


def reduced(request):
    message = request.GET['message']
    temp = Reducer.objects.create(url=message)
    return render(request, './reducer/reduced.html', {'message': temp.key})


def get_link(request, key):
    temp = Reducer.objects.get(key=key)
    return redirect(temp.url)
