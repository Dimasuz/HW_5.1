from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Measurement(models.Model):
    id = models.AutoField(primary_key=True)
    temperature = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='smart_home/photo', null=True, blank=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    def __str__(self):
        return self.sensor
