# Generated by Django 5.0.2 on 2024-02-20 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xkom', '0002_itemmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmodel',
            name='link',
            field=models.CharField(max_length=200, unique=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='itemmodel',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nazwa'),
        ),
    ]