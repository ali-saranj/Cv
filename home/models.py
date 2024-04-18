from django.db import models
from django.urls import reverse


# Create your models here.

# Create your models here.

# user
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=500)

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


# blog
class Post(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.pk])

    def __str__(self):
        return self.title
