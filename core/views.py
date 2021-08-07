from rest_framework import generics, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .dto import CompanyListDto, DiscountDto
from .filters import get_filter_company_and_city
from .models import Review, Category
from .serializers import CompanySerializer, DiscountDetailSerializer, GetCouponSerializer, ReviewSerializer, \
    CategorySerializer, ActivateCouponSerializer
from .services.view_service import counts_views, get_object, is_exist_client_or_discount


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
    """Получение купона и создание операции"""

    def post(self, request):
        serializer = GetCouponSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivateCouponView(APIView):
    """Активация купона"""

    def post(self, request):
        serializer = ActivateCouponSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            discount_id, client_id = serializer.data['discount'], serializer.data['client']
            operation = is_exist_client_or_discount(discount_id, client_id)
            operation.status = '1'
            operation.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
