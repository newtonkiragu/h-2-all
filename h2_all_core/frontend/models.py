from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.

class Price(models.Model):
    per_litre = models.PositiveIntegerField()
    name = models.CharField(max_length=256)

class Borehole(models.Model):
    id = models.IntegerField(primary_key=True)
    phone_number = models.IntegerField(default=2547200000)
    location = models.CharField(max_length=256)
    price = models.ForeignKey(Price, related_name='bore_holes', null=False, blank=False, on_delete="cascade")




class Stat(models.Model):
    bore_hole = models.ForeignKey(Borehole, related_name='stats', null=True, on_delete="cascade")
    data = JSONField()
