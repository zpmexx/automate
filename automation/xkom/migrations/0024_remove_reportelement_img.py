# Generated by Django 5.0.2 on 2024-03-06 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xkom', '0023_alter_reportelement_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportelement',
            name='img',
        ),
    ]
