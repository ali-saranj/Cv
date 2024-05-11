from django.db import models
from django.urls import reverse
from jalali_date import date2jalali, date2jalali


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


# content
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    description = models.TextField()

    def __str__(self):
        return f"{self.pk}_{self.name}"


class Grouping(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.pk}_{self.name}"


# blog
class Post(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    is_featured = models.BooleanField(default=False)
    Grouping = models.ForeignKey(Grouping, on_delete=models.PROTECT, null=True)

    class Meta:
        permissions = [
            ("can_add_post", "Can add post"),
            ("can_change_post", "Can change post"),
            ("can_delete_post", "Can delete post"),
        ]

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.pk])

    # def get_time(self):
    #     return date2jalali(self.pub_date)

    def __str__(self):
        return self.title


class Coment_Posts(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    content = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.pk}_{self.name}"


# ارتباط با ما در صفحه پلن
class Contact_us(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    location = models.TextField()

    def __str__(self):
        return f"{self.pk}_{self.name}"

