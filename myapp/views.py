from django.shortcuts import render
from .models import getdata
# Create your views here.

def index(requests):
    return render(request, 'index.html')