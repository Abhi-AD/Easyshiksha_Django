from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from music.models import Albume, Song


# Create your views here.
def index(request):
    all_albums = Albume.objects.all()
    context = {"all_albums": all_albums}
    return render(request, "music/index.html", context)


def albume_details(request, albume_id):
    # albume = Albume.objects.get(pk=albume_id)
    albume = get_object_or_404(Albume, pk=albume_id)
    return render(request, "music/details.html", {"albume": albume})


def favorite(request, albume_id):
    albume = get_object_or_404(Albume, pk=albume_id)
    try:
        select_song = albume.song_set.get(pk=request.POST["song"])
    except (KeyError, Song.DoesNotExist):
        return render(
            request,
            "music/details.html",
            {"albume": albume, "error_message": "You did not select a valid song"},
        )
    else:
        select_song.is_favorite = True
        select_song.save()
        return render(request, "music/details.html", {"albume": albume})
