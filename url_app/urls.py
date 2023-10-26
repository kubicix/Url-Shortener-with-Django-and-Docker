# urls.py

from django.urls import path
from .views import shorten_url, redirect_original

urlpatterns = [
    path('', shorten_url, name='index'),
    path('<str:short_url>/', redirect_original, name='redirect_original'),
    # Diğer URL'leri buraya ekleyebilirsiniz.
]
