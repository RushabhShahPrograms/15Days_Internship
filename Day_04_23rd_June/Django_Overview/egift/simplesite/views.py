from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

'''
def index(request):
    return HttpResponse("Hello World. You're at the simplesite index.")
'''

def aboutUs(request):
    return render(request,"simplesite/aboutus.html")

def aboutYou(request):
    return render(request,"simplesite/aboutyou.html")

def privacyPolicy(request):
    return render(request,"simplesite/privacypolicy.html")

def termsAndCondition(request):
    return render(request,"simplesite/termsandcondition.html")