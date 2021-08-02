from itertools import chain

from core.models import Company, City


def get_filter_company_and_city(query_param):
    category_name_query = query_param.get('category')
    city_query = query_param.get('city')
    company_queryset = Company.objects.all()
    if category_name_query:
        company_queryset = company_queryset.filter(category__name=category_name_query)

    company_and_city_queryset = company_queryset.filter(location__city__name=city_query).order_by("company__order_num")
    get_exclude = Company.objects.exclude(location__city__name=city_query).order_by("company__order_num")

    return list(chain(company_and_city_queryset, get_exclude))





