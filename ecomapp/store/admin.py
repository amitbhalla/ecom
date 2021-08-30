from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "id",
    ]
    prepopulated_fields = {
        "slug": ("name",),
    }
    readonly_fields = ("id",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "slug",
        "price",
        "in_stock",
        "created",
        "updated",
        "id",
    ]
    list_filter = [
        "in_stock",
        "is_active",
    ]
    list_editable = [
        "price",
        "in_stock",
    ]
    prepopulated_fields = {
        "slug": ("title",),
    }
    readonly_fields = ("id",)
