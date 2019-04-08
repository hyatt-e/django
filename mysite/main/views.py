from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# HttpResponse lets us respond to requests with html
def homepage(request):
	return HttpResponse("Wow what an awesome web page")
