# Generated by Django 5.0.2 on 2024-02-27 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xkom', '0006_alter_reportelement_creation_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportelement',
            name='creation_date',
        ),
    ]
