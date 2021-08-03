from django.http import Http404
from requests import Response
from rest_framework.exceptions import ValidationError

from core.models import View, Company, Operation, Discount, Client


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
        raise ValidationError


def get_discount_object(pk_discount):
    try:
        return Discount.objects.get(pk=pk_discount)
    except Discount.DoesNotExist:
        raise ValidationError


def get_client_object(pk_client):
    try:
        return Client.objects.get(id=pk_client)
    except Client.DoesNotExist:
        raise ValidationError


def add_operation(pk_discount, pk_client):
    """Создает операцию по Id скидки и по id клиента"""
    operation = Operation.objects.filter(discount=pk_discount, client=pk_client)
    if operation:
        # raise ValidationError({'error': 'Купон уже использован'})
        pass
    discount_obj = get_discount_object(pk_discount)
    client_obj = get_client_object(pk_client)
    operation = Operation.objects.create(client=client_obj,
                                         discount=discount_obj)
