from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Albume
from music.forms import UserFrom


class IndexView(generic.ListView):
    template_name = "music/index.html"
    context_object_name = "all_albums"

    def get_queryset(self):
        return Albume.objects.all()


class Albume_DetailView(generic.DetailView):
    model = Albume
    template_name = "music/details.html"


class Albume_CreateView(CreateView):
    model = Albume
    fields = ["artist", "albume_title", "genre", "albume_logo"]


class Albume_UpdateView(UpdateView):
    model = Albume
    fields = ["artist", "albume_title", "genre", "albume_logo"]


class Albume_DeleteView(DeleteView):
    model = Albume
    success_url = reverse_lazy("music:index")


class UserFormView(View):
    form_class = UserFrom
    template_name = "music/registration_form.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # cleaned data
            username = form.cleaned_data("username")
            password = form.cleaned_data("password")
            user.set_password(password)
