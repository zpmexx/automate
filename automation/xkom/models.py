from django.db import models
from PIL import Image
# Create your models here.
from io import BytesIO
from django.core.files.base import ContentFile

import datetime
status = [
    (0, ("Aktywne")),
    (1, ("Nieaktywne")),
]

class ItemModel(models.Model):
    name = models.CharField(verbose_name="Nazwa", max_length=200, blank = True)
    link = models.CharField(verbose_name="Link", max_length=200, unique = True)
    target_price = models.FloatField(null = False, blank = False, default = 0.0, verbose_name="Cena docelowa")
    current_price = models.FloatField(null = False, blank = False, default = 0.0, verbose_name="Cena obecna")
    category = models.CharField(verbose_name="Kategoria", max_length=200, blank = True)
    img = models.ImageField(upload_to='images/', default='images/default.jpg', verbose_name="Zdjęcie")
    status =  models.IntegerField(choices=status, default=0, verbose_name='Status')
    
    def __str__(self):
        return str(f'{self.name}')

    class Meta:
        verbose_name = "Przedmiot"
        verbose_name_plural = "Przedmioty"
        
    def save(self, *args, **kwargs):
        super().save()
        
        image = Image.open(self.img.path)
        
        if image.height > 300 or image.width > 300:
            image.thumbnail((300,300))
            image.save(self.img.path)
            

class ReportElement(models.Model):
    item_name = models.CharField(verbose_name="Nazwa Przedmiotu", max_length=200, blank = True)
    link = models.CharField(verbose_name="Link przedmiotu", max_length=200)
    target_price = models.FloatField(null = False, blank = False, default = 0.0, verbose_name="Cena docelowa")
    current_price = models.FloatField(null = False, blank = False, default = 0.0, verbose_name="Cena obecna")
    starting_price = models.FloatField(null = True, blank = True, default = 0.0, verbose_name="Cena Wyjściowa")
    difference =  models.FloatField(null = False, blank = False, default = 0.0, verbose_name="Różnica")
    full_difference =  models.FloatField(null = True, blank = True, default = 0.0, verbose_name="Pełna różnica")
    creation_date =  models.DateTimeField(verbose_name='Data utworzenia', auto_now_add=True)
    img = models.ImageField(upload_to='images/', default='images/default.jpg', verbose_name="Zdjęcie", blank=True, null=True)
    
    def save(self, *args, **kwargs):
        print(self.full_difference)
        print(type(self.full_difference))
        try:
            item = ItemModel.objects.get(link=self.link)
            self.img = item.img  
        except ItemModel.DoesNotExist:
            self.img = 'images/default.jpg'
        try:
            self.starting_price = item.current_price
        except:
            pass
        if self.difference == 0.0 or not self.difference:
            self.difference = self.target_price - self.current_price
        if self.full_difference == 0.0 or not self.full_difference:
            self.full_difference = self.starting_price - self.current_price
        
        
        super(ReportElement, self).save(*args, **kwargs)