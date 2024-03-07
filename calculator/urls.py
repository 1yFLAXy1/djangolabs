from django.urls import path
from . import views


urlpatterns = [
    path('', views.calculate, name='calculate'),  # Додано шлях для кореневого URL
]

