# Generated by Django 5.0.2 on 2024-02-27 10:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xkom', '0005_reportelement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportelement',
            name='creation_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]