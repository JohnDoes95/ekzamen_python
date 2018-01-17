from django import forms
from django.contrib import admin
from .models import Category, Products
from django.core.urlresolvers import reverse


class CategoryCreatedForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = ()


class CategoryCreated(admin.ModelAdmin):
    form = CategoryCreatedForm
    list_display = ('name', 'created_at', 'updated_at', )
    readonly_fields = ('updated_at', 'created_at', )


class ProductCreatedForm(forms.ModelForm):

    class Meta:
        model = Products
        exclude = ()


class ProductsCreated(admin.ModelAdmin):
    form = ProductCreatedForm
    list_display = ('name', 'description', 'images', 'price', 'in_stock', 'category', )

    def get_categorys(self, obj):
        link = reverse('admin:ekzamen_shop_product_change', args=[obj.product.id])
        return '<a href="{}">{}</a>'.format(link, obj.product.name)
    get_categorys.admin_order_field = 'product__name'
    get_categorys.short_description = 'Product name'
    get_categorys.allow_tags = True


admin.site.register(Category, CategoryCreated)
admin.site.register(Products, ProductsCreated)
