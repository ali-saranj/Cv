# Generated by Django 4.2.10 on 2024-04-18 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_author_users_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.author_users'),
        ),
    ]
