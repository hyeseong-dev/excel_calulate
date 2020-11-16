from django.shortcuts import render
from django.http.response import HttpResponse


def calculate(request):
    return HttpResponse('calculate, calculate function!')
