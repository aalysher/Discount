from datetime import datetime

import pytz
from django.utils import timezone
from pytz import utc

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Company, Discount, Location, SocialMedia, Review, Category, Operation
from .services.view_service import is_exist_operation


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
    location = LocationDetailSerializer(many=True)
    condition = serializers.CharField()
    instruction = serializers.CharField()

    class Meta:
        model = Discount
        exclude = ("pin", "order_num", "company")


class ReviewSerializer(serializers.ModelSerializer):
    # client = serializers.SlugRelatedField(slug_field='id', read_only=True)
    class Meta:
        model = Review
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class GetCouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ('discount', 'client')

    def create(self, validated_data):
        deadline = datetime.now() + validated_data['discount'].coupon_duration
        coupon = Operation.objects.create(discount=validated_data['discount'],
                                          client=validated_data['client'],
                                          deadline=deadline)
        return coupon

    def validate(self, data):
        discount = data['discount']
        client = data['client']
        amount_coupons = Operation.objects.filter(discount=data['discount'], status__in=['1', '2'])
        if is_exist_operation(client, discount):
            if len(amount_coupons) >= discount.company.limit:
                discount.company.active = False
                discount.company.save()
                raise ValidationError("Превышен лимит")
            return data

    def to_representation(self, instance):
        return {'percent': instance.discount.percent, 'condition': instance.discount.condition,
                'company': instance.discount.company.name, 'купон действует до': instance.deadline.strftime('%d.%m.%Y %H:%M')}


class ActivateCouponSerializer(serializers.ModelSerializer):
    pin = serializers.IntegerField()

    class Meta:
        model = Operation
        fields = ("pin", "client", "discount")

    def validate(self, data):
        pin = data['pin']
        discount = data['discount']
        client = data['client']
        status = Operation.objects.get(discount_id=discount.id, client_id=client.id).status

        deadline = Operation.objects.get(discount_id=discount.id, client_id=client.id).deadline
        local_tz = pytz.timezone('Asia/Kolkata')
        current_datetime = datetime.now().replace(tzinfo=pytz.utc).astimezone(local_tz)
        expired_on = deadline.replace(tzinfo=pytz.utc).astimezone(local_tz)
        if current_datetime >= expired_on:
            Operation.objects.update(status='3')
            raise ValidationError('Срок действия купона завершен')
        elif pin != int(discount.pin):
            raise ValidationError('Неверный пин')
        elif status == '1':
            raise ValidationError('Купон уже активирован')
        return data
