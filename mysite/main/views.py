# render ...renders... an HTML page
from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial

# Create your views here.


# HttpResponse lets us respond to requests with html
def homepage(request):
    return render(request=request,
                  template_name="main/home.html",
                  context={"tutorials": Tutorial.objects.all}
                  )
