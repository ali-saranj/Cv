# Generated by Django 4.2.10 on 2024-04-18 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_post_author_delete_author_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
