from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import ItemModel

class ItemModelAdmin(admin.ModelAdmin):
    
    def image_tag(self, obj):
        return format_html(f'<img src="{obj.img.url}" style="max-width:100px; max-height:100px"/>')
    
    list_display = ['image_tag','name','target_price','current_price','status']
    search_fields = ['name']
    ordering = ['name']
    list_filter = ['status']

admin.site.register(ItemModel, ItemModelAdmin)