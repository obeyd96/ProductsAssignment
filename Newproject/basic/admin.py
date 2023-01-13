from django.contrib import admin
from .models import Product, ProductColour, ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'unique_code')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductColour)
admin.site.register(ProductImage)
