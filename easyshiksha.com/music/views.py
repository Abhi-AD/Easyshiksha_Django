from django.shortcuts import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>This is a music app in home</h1>")


def albume_details(request, albume_id):
    return HttpResponse(f"<h2>Details for Album id: {albume_id}</h2>")
