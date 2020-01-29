from django.urls import path
from .views import lot

urlpatterns = [
    path('hello/',lot.as_view(),name='home'),
]