from django.db import models

class Tur(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Gul(models.Model):
    tur = models.ForeignKey(Tur, on_delete=models.CASCADE, related_name='gullar')
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name
