from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import ItemModel

class ItemModelAdmin(admin.ModelAdmin):
    
    def image_tag(self, obj):
        return format_html(f'<img src="{obj.img.url}" style="max-width:100px; max-height:100px"/>')
    
    def html_link(self, obj):
        return format_html(f'<a href="{obj.link}" target=”_blank” >{obj.link}</a>')
    
    list_display = ['image_tag','name','html_link','target_price','current_price','status','category']
    search_fields = ['name','category']
    ordering = ['name']
    list_filter = ['status']

admin.site.register(ItemModel, ItemModelAdmin)