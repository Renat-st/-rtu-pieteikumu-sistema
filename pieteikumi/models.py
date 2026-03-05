from django.db import models

class Pieteikums(models.Model):
    nosaukums = models.CharField(max_length=200)
    apraksts = models.TextField()
    statuss = models.CharField(max_length=50, default="NEW")

    def __str__(self):
        return self.nosaukums

