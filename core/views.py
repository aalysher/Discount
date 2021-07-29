from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination

from .dto import CompanyListDto, DiscountDto
# from .filters import CompanyFilter
from .models import Discount, Company, Review, Category
from .serializers import CompanySerializer, DiscountDetailSerializer, CouponSerializer, ReviewSerializer, \
    CategorySerializer
from .services.view_service import counts_views, get_object


class CompanyList(generics.ListAPIView):
    """Список всех компаний предоставляющие скидки"""
    queryset = CompanyListDto().company_list_dto
    serializer_class = CompanySerializer
    pagination_class = LimitOffsetPagination
    # filter_backends = (DjangoFilterBackend,)
    # filterset_class = CompanyFilter


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
    queryset = Review.objects.create()
    serializer_class = ReviewSerializer


class CategoryList(generics.ListAPIView):
    """Список всех категорий"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CouponCreateUpdateView(generics.ListAPIView):
    """Создание купона и измение его статуса """
    queryset = Discount.objects.all()
    serializer_class = CouponSerializer
