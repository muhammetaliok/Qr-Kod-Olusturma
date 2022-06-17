from unicodedata import category
from django.shortcuts import render
from .models import QrCode
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from email import message
from multiprocessing import context
from telnetlib import PRAGMA_HEARTBEAT
from urllib.parse import urlencode
from django.contrib import messages

from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.
def home(request):
   if request.method=="POST":
      Url=request.POST['url']
      name=request.POST['name']
      get_email=request.POST['get_email']
      phone = request.POST['phone']
      QrCode.objects.create(url=Url,get_email=get_email,name=name,phone=phone)

   qr_code=QrCode.objects.all()
   return render(request,"home.html",{'qr_code':qr_code})








