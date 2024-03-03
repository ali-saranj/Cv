from django.db import models
from django.urls import reverse

# Create your models here.

# Create your models here.

class Plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return f"{self.pk}_{self.name}"


class Project(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('contact')

    def __str__(self):
        return f"{self.pk}_{self.name}"