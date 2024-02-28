from django.contrib import admin
from django.utils.html import format_html
from .models import ItemModel
from django.contrib.admin import SimpleListFilter
from django.db.models import Count

class CategoryCountFilter(SimpleListFilter):
    title = 'category'
    parameter_name = 'category'

    def lookups(self, request, model_admin):
        # Generate a queryset that counts items per unique category value
        categories = (
            ItemModel.objects
            .values('category')  # Group by 'category'
            .annotate(item_count=Count('id'))  # Count items per category
            .order_by('-item_count')  # Ensure a consistent order
        )
        # Format the choices as ('category', 'category (count)') tuples
        return [(category['category'], f"{category['category']} ({category['item_count']})") for category in categories]

    def queryset(self, request, queryset):
        # Filter the queryset based on the selected category, if any
        if self.value():
            return queryset.filter(category=self.value())
        else:
            return queryset


class ItemModelAdmin(admin.ModelAdmin):
    
    def image_tag(self, obj):
        return format_html(f'<img src="{obj.img.url}" style="max-width:100px; max-height:100px"/>')
    
    def html_link(self, obj):
        return format_html(f'<a href="{obj.link}" target=”_blank” >{obj.link}</a>')
    
    list_display = ['image_tag','name','html_link','target_price','current_price','status','category']
    search_fields = ['name','category']
    ordering = ['name']
    list_filter = ['status',CategoryCountFilter]

admin.site.register(ItemModel, ItemModelAdmin)