# Generated by Django 3.1.7 on 2021-03-22 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='Id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]