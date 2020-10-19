from django.contrib import admin

# Register your models here.
from .models import *


class ColorAdmin(admin.ModelAdmin):
    list_display = ['color']
admin.site.register(Color, ColorAdmin)


class RouseCountAdmin(admin.ModelAdmin):
    list_display = ['rouse']
admin.site.register(RouseCount, RouseCountAdmin)


class ColorTypeAdmin(admin.ModelAdmin):
    list_display = ['color_type']
admin.site.register(ColorType, ColorTypeAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'rouse', 'color','price', 'color_type', 'color_type2', 'color_type3', 'description', 'slug', 'available', 'created', 'updated']
    list_filter = ['available','rouse', 'color', 'color_type', 'created', 'updated']
    list_editable = ['rouse', 'color', 'color_type', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)