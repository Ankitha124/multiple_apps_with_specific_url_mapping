from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sinchana(request):
    return HttpResponse('<h1>Sinchana is a good girl')

