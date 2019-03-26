from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    genere = models.CharField(max_length=100)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', Kwarggs={'pk':self.pk})

    def __str__(self):
        return f'{self.title} by {self.artist}'

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=30)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.song_title} from {self.album}'