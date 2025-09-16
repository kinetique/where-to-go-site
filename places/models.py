from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    place_type = models.CharField(max_length=50, choices=())
    location = models.CharField(max_length=100, blank=True, null=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.URLField(blank=True, null=True)
