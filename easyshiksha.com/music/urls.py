from django.urls import path
from music import views

app_name = "music"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.Albume_DetailView.as_view(), name="albume_details"),
    # path("<int:albume_id>/favorite", views.favorite, name="favorite"),
]
