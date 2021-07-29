from django.http import Http404

from core.models import View, Company


def counts_views(company):
    """Считает просмотры при входе в детальную выборку скидок"""
    views = View.objects.get(pk=company.id)
    views.counter += 1
    views.save()


def get_object(pk):
    """Валидация на не существущий id"""
    try:
        return Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        raise Http404
