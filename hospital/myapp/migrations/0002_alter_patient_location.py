# Generated by Django 4.1.3 on 2023-01-16 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='location',
            field=models.CharField(max_length=225),
        ),
    ]
