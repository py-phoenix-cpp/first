from django.shortcuts import render
from django.http import HttpResponse


def Index(request):

    return HttpResponse('<h1 style="color : red;">Salom dunyo</h1>')
