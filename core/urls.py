from django.urls import path

from core import views

urlpatterns = [
    path('list/', views.CompanyList.as_view()),
    # Список всех компаниий предоставляющие скидки
    path('list/<int:pk>/', views.DiscountDetail.as_view()),
    # Опредленная скидка про primary key
    path('coupon/<int:pk_discount>/<int:pk_client>/', views.CreateCouponOperation.as_view()),
    # Выдача купона
    path('review/', views.ReviewCreateView.as_view()),
    # Оставить отзыв
    path('category/', views.CategoryList.as_view())
    # Список всех категорий
]
