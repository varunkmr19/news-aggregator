from django.db import models

# Create your models here.


class Article(models.Model):
    IDEOLOGY = [
        ('LW', 'Left Wing'),
        ('RW', 'Right Wing')
    ]
    headline = models.CharField(max_length=255)
    url = models.URLField(unique=True, max_length=2000)
    ideology = models.CharField(choices=IDEOLOGY, max_length=10)
    image_url = models.TextField()
    published_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.headline
