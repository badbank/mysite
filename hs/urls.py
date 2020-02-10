from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:real_type_name>/<str:real_id>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('<str:real_type_name>/', views.typedetail, name='typedetail')
]
