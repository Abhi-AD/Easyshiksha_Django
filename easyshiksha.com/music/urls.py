from django.urls import path
from music import views

app_name = "music"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("register/", views.UserFormView.as_view(), name="register"),
    path("<int:pk>/", views.Albume_DetailView.as_view(), name="albume_details"),
    path("albume/add/", views.Albume_CreateView.as_view(), name="albume_create"),
    path("albume/<int:pk>/", views.Albume_UpdateView.as_view(), name="albume_update"),
    path(
        "albume/<int:pk>/delete",
        views.Albume_DeleteView.as_view(),
        name="albume_delete",
    ),
    # path("<int:albume_id>/favorite", views.favorite, name="favorite"),
]
