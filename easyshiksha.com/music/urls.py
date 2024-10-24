from django.urls import path
from music import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:albume_id>/", views.albume_details, name="albume_details"),
]
