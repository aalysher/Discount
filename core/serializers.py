from rest_framework import serializers

from .models import Company, Discount, Location, View, SocialMedia, City, Instruction, Review, Category


class CompanySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    photo = serializers.URLField()
    view = serializers.IntegerField()
    percent = serializers.IntegerField()
    city = serializers.CharField()

    class Meta:
        model = Company
        exclude = ('category',)


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ('type', 'link')


class LocationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('address', 'latitude', 'longitude')


class DiscountDetailSerializer(CompanySerializer):
    social_media = SocialMediaSerializer(many=True)
    location = LocationDetailSerializer()
    condition = serializers.CharField()
    instruction = serializers.CharField()

    class Meta:
        model = Discount
        exclude = ("pin", "order_num", "company")


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CouponSerializer(serializers.ModelSerializer):
    company = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Discount
        fields = ('percent', 'condition', 'company')
