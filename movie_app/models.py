from django.db import models


# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    duration = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='directors')

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField(max_length=400)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(default=1, choices=[(i, i * '*')for i in range(1, 6)])

    def __str__(self):
        return self.text