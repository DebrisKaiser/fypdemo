from django.urls import path
from .views import table_view, dashboard_view, test_view

urlpatterns = [
    path('table/', table_view, name='table'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('test/', test_view, name='test'),
]
