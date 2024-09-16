from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Song(models.Model):

    language_choice = (("Hindi", "Hindi"), ("English", "English"), ("Punjabi", "Punjabi"), ("Haryanvi", "Haryanvi"), ("Assamese", "Assamese"), ("Bhojpuri", "Bhojpuri"))

    name = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    artists = models.CharField(max_length=200)
    release_date = models.IntegerField()
    language = models.CharField(max_length=30, choices=language_choice, default="Hindi")
    song_thumbnail = models.FileField()
    song_mp3 = models.FileField()

    def __str__(self) -> str:
        return self.name


class Playlist(models.Model):
    playlist = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)


class Favourite(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    is_fav = models.BooleanField(default=False)


class Recent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
