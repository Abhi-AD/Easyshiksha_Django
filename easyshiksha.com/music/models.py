from django.db import models


# Create your models here.
class Albume(models.Model):
    artist = models.CharField(max_length=255)
    albume_title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    albume_logo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.artist} - {self.albume_title}"


class Song(models.Model):
    albume = models.ForeignKey(Albume, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=100)
    song_title = models.CharField(max_length=255)
