# Generated by Django 4.2.10 on 2024-05-02 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]