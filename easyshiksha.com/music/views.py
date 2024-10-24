from django.shortcuts import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>This is a music app in home</h1>")
