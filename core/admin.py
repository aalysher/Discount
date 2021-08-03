from django.contrib import admin

from .models import Company, Discount, Location, View, SocialMedia, Instruction, \
    Review, City, Category, Operation, Client


class CompanySettings(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')


class DiscountSettings(admin.ModelAdmin):
    list_display = ('id', 'company', 'order_num', 'percent', 'active', 'pin')


class LocationSettings(admin.ModelAdmin):
    list_display = ('id', 'city', 'address', 'company')


class InstructionSettings(admin.ModelAdmin):
    list_display = ('id', 'title')


class ReviewSettings(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'published_date')


class CategorySettings(admin.ModelAdmin):
    list_display = ('id', 'name')


class OperationSettings(admin.ModelAdmin):
    list_display = ('id', 'client', 'discount')


class ClientSettings(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'city')


admin.site.register(Company, CompanySettings)
admin.site.register(Discount, DiscountSettings)
admin.site.register(Location, LocationSettings)
admin.site.register(View)
admin.site.register(SocialMedia)
admin.site.register(Instruction, InstructionSettings)
admin.site.register(Review, ReviewSettings)
admin.site.register(City)
admin.site.register(Category, CategorySettings)
admin.site.register(Operation, OperationSettings)
admin.site.register(Client, ClientSettings)
