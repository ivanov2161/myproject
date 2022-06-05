from django.shortcuts import render, redirect
from .models import Url
import string
import secrets
alphabet = string.ascii_letters + string.digits


def home(request):
    return render(request, './reducer/home.html')


def reduced(request):
    message = request.GET['message']
    key = ''.join(secrets.choice(alphabet) for i in range(4))
    temp = Url.objects.create(key=key, url=message)
    return render(request, './reducer/reduced.html', {'message': temp.key})


def get_link(request, key):
    temp = Url.objects.get(key=key)
    return redirect(temp.url)
