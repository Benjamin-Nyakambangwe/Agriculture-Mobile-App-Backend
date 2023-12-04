from django.db import models

from users.models import Profile

def upload_to(instance, filename):
    return filename.format(filename=filename)

class Farm(models.Model):
    owner = models.ForeignKey(Profile, related_name='farms', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    cover = models.ImageField(upload_to=upload_to, blank=True, null=True)
    logo = models.ImageField(upload_to=upload_to, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.description[:20])
    

class Produce(models.Model):
    farm = models.ForeignKey(Farm, related_name='produce', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.description[:20])
    
    class Meta:
        ordering = ('-created_at',)
