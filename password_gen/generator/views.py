from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'home-page/home.html')

def password(request):
    resList = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        resList.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('nambers'):
        resList.extend(list('0123456789')) 
    if request.GET.get('special-chars'):
        resList.extend(list('!@#$%^&*()'))

    length = int(request.GET.get('length-pass', 8))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(resList)

    return render(request, 'password-page/password.html', {'password': thepassword})