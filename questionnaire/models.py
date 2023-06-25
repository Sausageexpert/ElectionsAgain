from django.db import models

class Questions(models.Model):
    def __str__(self):
        return self.question
    question = models.CharField(max_length=200)
    answers = models.CharField(max_length=200)
    identity = models.CharField(max_length=7)