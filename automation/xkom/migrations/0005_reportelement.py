# Generated by Django 5.0.2 on 2024-02-27 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xkom', '0004_itemmodel_category_alter_itemmodel_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=200, verbose_name='Nazwa Przedmiotu')),
                ('link', models.CharField(max_length=200, verbose_name='Link przedmiotu')),
                ('target_price', models.FloatField(default=0.0, verbose_name='Cena docelowa')),
                ('current_price', models.FloatField(default=0.0, verbose_name='Cena obecna')),
                ('difference', models.FloatField(default=0.0, verbose_name='Różnica')),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
