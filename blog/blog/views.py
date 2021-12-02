from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
# Create your views here.

def index(request):
    return HttpResponseRedirect(reverse('app_blog:BlogList'))