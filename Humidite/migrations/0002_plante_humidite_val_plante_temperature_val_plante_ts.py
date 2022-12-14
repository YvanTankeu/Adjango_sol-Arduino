# Generated by Django 4.1.2 on 2022-12-09 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Humidite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plante',
            name='humidite_val',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='plante',
            name='temperature_val',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='plante',
            name='ts',
            field=models.IntegerField(null=True),
        ),
    ]
