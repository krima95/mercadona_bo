from django.contrib import admin

from products.models import Category, Product, Promotion

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Promotion)

