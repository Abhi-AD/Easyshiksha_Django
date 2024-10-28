from django.views import generic
from .models import Albume


class IndexView(generic.ListView):
    template_name = "music/index.html"
    context_object_name = "all_albums"

    def get_queryset(self):
        return Albume.objects.all()


class Albume_DetailView(generic.DetailView):
    model = Albume
    template_name = "music/details.html"
