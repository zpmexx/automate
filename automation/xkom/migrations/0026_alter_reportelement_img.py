# Generated by Django 5.0.2 on 2024-03-06 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xkom', '0025_reportelement_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportelement',
            name='img',
            field=models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images/', verbose_name='Zdjęcie'),
        ),
    ]
