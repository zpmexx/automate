# Generated by Django 5.0.2 on 2024-02-29 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xkom', '0012_remove_reportelement_created_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportelement',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
