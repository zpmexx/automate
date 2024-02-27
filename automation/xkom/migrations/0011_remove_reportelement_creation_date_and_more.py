# Generated by Django 5.0.2 on 2024-02-27 10:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xkom', '0010_alter_reportelement_creation_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportelement',
            name='creation_date',
        ),
        migrations.AddField(
            model_name='reportelement',
            name='created_datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
