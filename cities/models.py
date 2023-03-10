from django.db import models


# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = "Cities"
        ordering = ('name',)
