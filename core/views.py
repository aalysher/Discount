from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .dto import CompanyListDto, DiscountDto
from .filters import get_filter_company_and_city
from .models import Discount, Review, Category, Operation, Client
from .serializers import CompanySerializer, DiscountDetailSerializer, CouponSerializer, ReviewSerializer, \
    CategorySerializer
from .services.view_service import counts_views, get_object


class CompanyList(generics.ListAPIView):
    """Список всех компаний предоставляющие скидки"""
    serializer_class = CompanySerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        filtered_company = get_filter_company_and_city(self.request.query_params)
        queryset = CompanyListDto(filtered_company).company_list_dto
        return queryset


class DiscountDetail(APIView):
    """Получение компании по id"""

    def get(self, request, pk):
        company = get_object(pk)
        company_dto = DiscountDto(company)
        counts_views(company)
        serializer = DiscountDetailSerializer(company_dto)
        return Response(serializer.data)


class ReviewCreateView(generics.CreateAPIView):
    """Создание отзыва клиента"""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CategoryList(generics.ListAPIView):
    """Список всех категорий"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CreateCouponOperation(APIView):
    """Создание купона и измение его статуса """

    def get(self, request, pk_discount, pk_client):
        queryset = Discount.objects.get(pk=pk_discount)
        serializer = CouponSerializer(queryset)

        operation = Operation.objects.filter(discount=pk_discount, client=pk_client)

        if operation:
            raise ValidationError({'error': 'Купон уже использован'})

        discount_obj = Discount.objects.get(id=pk_discount)
        client_obj = Client. objects.get(id=pk_client)

        operation = Operation.objects.create(client=client_obj,
                                             discount=discount_obj)

        data = serializer.data

        data['Срок окончания купона'] = operation.start_date + discount_obj.deadline
        return Response(data)

    def post(self, request, pk_discount, pk_client):
        operation = Operation.objects.get(client_id=pk_client, discount_id=pk_discount)
        discount_deadline = operation.start_date + operation.discount.deadline
        return Response()
