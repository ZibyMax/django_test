from django.contrib import admin
from .models import Product, ProductInfo


class ProductAdmin(admin.ModelAdmin):
    pass


class ProductInfoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)

admin.site.register(ProductInfo, ProductInfoAdmin)
