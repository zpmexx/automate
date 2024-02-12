from django.db import models
from PIL import Image
# Create your models here.
from io import BytesIO
from django.core.files.base import ContentFile

class ItemModel(models.Model):
    name = models.CharField(verbose_name="Nazwa", blank=False, null=False, default = "nolink", max_length=200)
    link = models.CharField(verbose_name="Link", blank=False, null=False, default = "nolink", max_length=200)
    target_price = models.FloatField(null = False, blank = False, default = 0.0, verbose_name="Cena docelowa")
    current_price = models.FloatField(null = False, blank = False, default = 0.0, verbose_name="Cena obecna")
    img = models.ImageField(upload_to='images/', default='images/default.jpg', verbose_name="Zdjęcie")
    
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
            