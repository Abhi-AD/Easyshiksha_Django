from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from music.models import Albume


# Create your views here.
def index(request):
    all_albums = Albume.objects.all()
    context = {"all_albums": all_albums}
    return render(request, "music/index.html", context)


def albume_details(request, albume_id):
    # albume = Albume.objects.get(pk=albume_id)
    albume = get_object_or_404(Albume, pk=albume_id)
    return render(request, "music/details.html", {"albume": albume})
