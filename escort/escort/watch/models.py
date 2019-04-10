from django.db import models
from collections import OrderedDict

# Create your models here.
class Firefighter(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    specialty = models.CharField(max_length=60,null=True)
    sim_ccid = models.CharField(max_length=60,null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def display(self):
        data = OrderedDict()
        data['id'] = self.id
        data['first_name'] = self.first_name
        data['last_name'] = self.last_name
        data['full_name'] = self.first_name + ' ' + self.last_name
        data['specialty'] = self.specialty
        data['sim_ccid'] = self.sim_ccid
        data['active'] = self.active

        return data

class GasReading(models.Model):
    firefighter = models.ForeignKey(Firefighter, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True, blank=True)
    value = models.FloatField()

    def __str__(self):
        return str(self.value)

    def display(self):
        data = OrderedDict()
        data['id'] = self.id
        data['firefighter'] = self.firefighter
        data['created_at'] = self.created_at
        data['value'] = self.value

        return data

class TempReading(models.Model):
    firefighter = models.ForeignKey(Firefighter, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True, blank=True)
    value = models.FloatField()

    def __str__(self):
        return str(self.value)

    def display(self):
        data = OrderedDict()
        data['id'] = self.id
        data['firefighter'] = self.firefighter
        data['created_at'] = self.created_at
        data['value'] = self.value

class Location(models.Model):
    firefighter = models.ForeignKey(Firefighter, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    