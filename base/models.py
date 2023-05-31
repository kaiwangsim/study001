from django.db import models

# Create your models here.

class roomclass(models.Model):
    #host =
    #topic =
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class device(models.Model):
    #host =
    #topic =
    device_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    #participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    IP_add = models.GenericIPAddressField()

    def __str__(self):
        return f'device: {self.device_name} {self.IP_add}'
    
