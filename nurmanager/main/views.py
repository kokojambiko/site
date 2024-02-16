from django.shortcuts import render
from django.http import HttpResponse


def index(reguest):
    return render(reguest, 'main/star.html')


def nur(reguest):
    return render(reguest, 'main/nur.html')