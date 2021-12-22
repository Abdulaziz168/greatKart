from django.contrib import admin
from store.models import Product, Variation


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'id', 'price', 'stock', 'category', 'modified_date', 'is_available', 'images')
    prepopulated_fields = {'slug': ('product_name',)}


admin.site.register(Product, ProductAdmin)


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active', 'created_date')
    list_editable = ['is_active']
    list_filter = ('product', 'variation_category', 'variation_value', 'is_active')


admin.site.register(Variation, VariationAdmin)
