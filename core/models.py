from datetime import datetime, timedelta

from django.db import models


class Company(models.Model):
    """Компания предоставляющая скидку"""
    name = models.CharField("Название",
                            max_length=255)
    description = models.TextField("Описание")
    photo = models.URLField(blank=True, null=True)
    category = models.ForeignKey("Category",
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return self.name


class Discount(models.Model):
    """Бонускные Скидки"""
    pin = models.CharField("Пин-код",
                           max_length=20)
    order_num = models.IntegerField("Приоритет по фильтрации")
    percent = models.IntegerField("Процент скидки")
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(default=datetime(2999, 12, 31))
    condition = models.CharField("Условие",
                                 max_length=255)
    active = models.BooleanField("Статус",
                                 default=True)
    deadline = models.DurationField("Срок действия купона", default=timedelta())
    instruction = models.ForeignKey("Instruction",
                                    on_delete=models.CASCADE)
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                related_name="company")

    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"
        ordering = ("order_num",)

    def __str__(self):
        return str(self.company)


class Instruction(models.Model):
    """Инструкция по использованию скидочного купона"""
    title = models.CharField("Заголовок",
                             max_length=255)
    body = models.TextField("Текст")

    class Meta:
        verbose_name = "Инструкция"
        verbose_name_plural = "Инструкции"

    def __str__(self):
        return self.title


class Review(models.Model):
    """Отзыв"""
    client_name = models.CharField("Имя пользователя",
                                   max_length=255, blank=True, null=True)

    text = models.TextField("Текст отзыва")
    published_date = models.DateTimeField("Дата публикации отзыва",
                                          auto_now_add=True)
    discount = models.ForeignKey(Discount,
                                 on_delete=models.CASCADE,
                                 related_name='discount')
    client = models.ForeignKey("Client",
                               on_delete=models.CASCADE,
                               related_name="client")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.client_name


class City(models.Model):
    """Город"""
    name = models.CharField("Название города",
                            max_length=255)
    order_num = models.IntegerField("Фильтрация по приоритету")

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name


class Location(models.Model):
    """Локация"""
    city = models.ForeignKey(City,
                             on_delete=models.CASCADE)
    address = models.CharField("Адрес",
                               max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                related_name="location")

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.address


class View(models.Model):
    """Просмотры"""
    id = models.ForeignKey(Company,
                           primary_key=True,
                           unique=True,
                           on_delete=models.CASCADE)
    counter = models.IntegerField("Количество просмотров",
                                  default=0)

    class Meta:
        verbose_name = "Просмотр"
        verbose_name_plural = "Просмотры"

    def __str__(self):
        return str(self.counter)


class SocialMedia(models.Model):
    """Социальные сети"""
    type = models.CharField("Тип социальной сети",
                            max_length=255)
    link = models.URLField(blank=True,
                           null=True)
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"

    def __str__(self):
        return self.type


class Category(models.Model):
    """Категории товаров"""
    name = models.CharField("Название категории",
                            max_length=255)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


operation_choices = [('1', 'Активирован'),
                     ('2', 'Неактивирован'),
                     ('3', 'Просрочен')]


class Operation(models.Model):
    """Создание операции при выдаче скидочного купона"""
    client = models.ForeignKey("Client",
                               on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount,
                                 on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField("Статус операции", max_length=255,
                              choices=operation_choices,
                              default='2')

    class Meta:
        verbose_name = "Операция"
        verbose_name_plural = "Операции"

    def __str__(self):
        return str(self.client)


class Client(models.Model):
    """Клиент для получения скидочного купона"""
    first_name = models.CharField("Имя клиента",
                                  max_length=255)
    last_name = models.CharField("Фамилия клиента",
                                 max_length=255)
    city = models.ForeignKey(City,
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
