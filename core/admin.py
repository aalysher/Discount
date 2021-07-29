from django.contrib import admin

from .models import Company, Discount, Location, View, SocialMedia, Instruction, Review, City, Category


class CompanySettings(admin.ModelAdmin):
    list_display = ('id', 'name')


class DiscountSettings(admin.ModelAdmin):
    list_display = ('company', 'order_num', 'percent', 'active', 'category', 'pin')


class LocationSettings(admin.ModelAdmin):
    list_display = ('city', 'address', 'company')


class InstructionSettings(admin.ModelAdmin):
    list_display = ('id', 'title')


class ReviewSettings(admin.ModelAdmin):
    list_display = ('id', 'name', 'published_date')


class CategorySettings(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Company, CompanySettings)
admin.site.register(Discount, DiscountSettings)
admin.site.register(Location, LocationSettings)
admin.site.register(View)
admin.site.register(SocialMedia)
admin.site.register(Instruction, InstructionSettings)
admin.site.register(Review, ReviewSettings)
admin.site.register(City)
admin.site.register(Category, CategorySettings)
