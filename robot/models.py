from django.db import models

class Robot(models.Model):
    name = models.CharField(max_length=100)
    gold_collected = models.IntegerField(default=0)
    

    def __str__(self):
        return self.name

class Program(models.Model):
    pass


