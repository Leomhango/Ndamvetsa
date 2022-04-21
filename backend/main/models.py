from pyexpat import model
from statistics import mode
from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=255)
    part_of_speech = models.CharField(max_length=50)
    description = models.TextField()
    inSentence = models.TextField()

    def __str__(self):
        return self.word