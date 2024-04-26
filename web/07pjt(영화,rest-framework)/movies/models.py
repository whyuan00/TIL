from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    actors = models.ManyToManyField(Actor, related_name='movies') #영화를 찍은 배우! 다대다
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    poster_path = models.TextField()

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE) #영화 외래키
    title = models.CharField(max_length=100)                    #영화 제목
    content = models.TextField()

