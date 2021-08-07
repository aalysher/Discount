from datetime import datetime, timedelta

from rest_framework.exceptions import ValidationError

from core.models import View, Company, Operation


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
        raise ValidationError('Не верный id компании')


def is_exist_operation(client, discount):
    """Валидация на существующий купон"""
    try:
        Operation.objects.get(discount=discount, client=client)
    except Operation.DoesNotExist:
        return True
    raise ValidationError('Вы уже получили купон')


def is_exist_client_or_discount(discount_id, client_id):
    """Валидация на id клиента и скидки"""
    try:
        return Operation.objects.get(discount=discount_id, client=client_id)
    except Operation.DoesNotExist:
        raise ValidationError()
