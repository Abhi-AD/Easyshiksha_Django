from django.urls import path
from music import views

app_name = "music"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:albume_id>/", views.albume_details, name="albume_details"),
    path("<int:albume_id>/favorite", views.favorite, name="favorite"),
]
