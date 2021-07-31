from core.models import Company


def get_filter_company(query_param):
    category_name_query = query_param.get('category')
    company_queryset = Company.objects.all()
    if category_name_query:
        company_queryset = Company.objects.filter(category__name=category_name_query).order_by()
    return company_queryset



