# Generated by Django 4.2.10 on 2024-04-18 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_author_users_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='author_Users',
        ),
    ]