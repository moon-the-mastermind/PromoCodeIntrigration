
from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('apply-promo/', views.apply_promo, name='apply_promo'),
]
