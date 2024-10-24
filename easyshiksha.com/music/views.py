from django.http import HttpResponse, Http404
from django.shortcuts import render
from music.models import Albume


# Create your views here.
def index(request):
    all_albums = Albume.objects.all()
    context = {"all_albums": all_albums}
    return render(request, "music/index.html", context)


def albume_details(request, albume_id):
    try:
        albume = Albume.objects.get(pk=albume_id)
    except Albume.DoesNotExist:
        raise Http404("Albume does not exist")
    return render(request, "music/details.html", {"albume": albume})
