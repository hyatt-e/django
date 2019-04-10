# render ...renders... an HTML page
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.


# HttpResponse lets us respond to requests with html
def homepage(request):
    return render(request=request,
                  template_name="main/home.html",
                  context={"tutorials": Tutorial.objects.all}
                  )


def register(request):
    # request by default is only GET. Must specify a POST request
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # save user
            user = form.save()
            # automatically log the user in
            login(request, user)
            # can redirect to <app_name>:<url>  or a path (like "/")
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = UserCreationForm
    return render(request,
                  "main/register.html",
                  context={"form":form})
