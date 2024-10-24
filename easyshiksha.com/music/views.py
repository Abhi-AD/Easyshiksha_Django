from django.shortcuts import HttpResponse
from music.models import Albume


# Create your views here.
def index(request):
    all_albums = Albume.objects.all()  # Use Album instead of Albume
    html = ""
    for album in all_albums:
        url = f"/music/{album.id}/"
        html += f'<a href="{url}">{album.albume_title}</a></br>'
    return HttpResponse(html)


def albume_details(request, albume_id):
    return HttpResponse(f"<h2>Details for Album id: {albume_id}</h2>")
