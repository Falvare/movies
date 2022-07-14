# Generated by Django 4.0.6 on 2022-07-13 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='movies',
            new_name='movie',
        ),
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]