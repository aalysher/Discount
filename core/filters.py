# from django_filters import rest_framework as filters
# from .models import Company
#
#
# class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
#     pass
#
#
# class CompanyFilter(filters.FilterSet):
#     name = CharFilterInFilter(field_name='Location__city')
#
#     class Meta:
#         model = Company
#         fields = ("city",)
