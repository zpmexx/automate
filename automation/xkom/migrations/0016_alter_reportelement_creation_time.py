# Generated by Django 5.0.2 on 2024-02-29 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xkom', '0015_alter_reportelement_creation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportelement',
            name='creation_time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
