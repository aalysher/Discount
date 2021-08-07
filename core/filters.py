from itertools import chain

from core.models import Company, City


def get_filter_company_and_city(query_param):
    category_id_query = query_param.get('category')
    city_id_query = query_param.get('city')
    company_queryset = Company.objects.filter(active=True)
    if category_id_query:
        company_queryset = company_queryset.filter(category__id=category_id_query)
    city_upper_queryset = company_queryset.filter(location__city__id=city_id_query).\
        order_by("company__order_num")
    city_down_queryset = company_queryset.exclude(location__city__id=city_id_query). \
        order_by("company__order_num")
    return list(chain(city_upper_queryset, city_down_queryset))

# def get_filter_company_and_city(query_param):
#     category_name_query = query_param.get('category')
#     city_query = query_param.get('city')
#     if city_query and category_name_query:
#         company_queryset = Company.objects.raw(f"""
#         SELECT * FROM "core_company"
#         INNER JOIN "core_discount"
#         ON ("core_company"."id" = core_discount."company_id")
#         INNER JOIN "core_location"
#         ON ("core_company"."id" = "core_location"."company_id")
#         LEFT JOIN "core_city"
#         ON ("core_location"."city_id" = "core_city"."id")
#         INNER JOIN "core_category"
#         ON ("core_company"."category_id" = "core_category"."id")
#         WHERE "core_category"."name" = "{category_name_query}"
#         OR "core_city"."name" = "{city_query}"
#         order by "core_city"."id", "core_discount"."order_num"
#         """)
#     company_queryset = Company.objects.filter(active=True)
#
    # return company_queryset
