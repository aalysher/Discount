from datetime import datetime

from django.db import models


class Company(models.Model):
    """Компания предоставляющая скидку"""
    name = models.CharField("Название",
                            max_length=255)
    description = models.TextField("Описание")
    photo = models.URLField(blank=True, null=True)
    category = models.ForeignKey("Category",
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


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
    instruction = models.ForeignKey("Instruction",
                                    on_delete=models.CASCADE)
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE)

    def __str__(self):
        return str(self.company)

    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"


class Instruction(models.Model):
    """Инструкция по использованию скидочного купона"""
    title = models.CharField("Заголовок",
                             max_length=255)
    body = models.TextField("Текст")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Инструкция"
        verbose_name_plural = "Инструкции"


class Review(models.Model):
    """Отзыв"""
    name = models.CharField("Имя пользователя",
                            max_length=255)
    text = models.TextField("Текст отзыва")
    published_date = models.DateTimeField("Дата публикации отзыва",
                                          auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class City(models.Model):
    """Город"""
    name = models.CharField("Название города",
                            max_length=255)
    order_num = models.IntegerField("Фильтрация по приоритету")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Location(models.Model):
    """Локация"""
    city = models.ForeignKey(City,
                             on_delete=models.CASCADE)
    address = models.CharField("Адрес",
                               max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"


class View(models.Model):
    """Просмотры"""
    id = models.ForeignKey(Company,
                           primary_key=True,
                           unique=True,
                           on_delete=models.CASCADE)
    counter = models.IntegerField("Количество просмотров",
                                  default=0)

    def __str__(self):
        return str(self.counter)

    class Meta:
        verbose_name = "Просмотр"
        verbose_name_plural = "Просмотры"


class SocialMedia(models.Model):
    """Социальные сети"""
    type = models.CharField("Тип социальной сети",
                            max_length=255)
    link = models.URLField(blank=True,
                           null=True)
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"


class Category(models.Model):
    """Категории товаров"""
    name = models.CharField("Название категории",
                            max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Operation(models.Model):
    """Создание операции при выдаче скидочного купона"""
    client = models.ForeignKey("Client",
                               on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return str(self.client)

    class Meta:
        verbose_name = "Операция"
        verbose_name_plural = "Операции"


class Client(models.Model):
    """Клиент для получения скидочного купона"""
    first_name = models.CharField("Имя клиента",
                                  max_length=255)
    last_name = models.CharField("Фамилия клиента",
                                 max_length=255)
    city = models.ForeignKey(City,
                             on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


