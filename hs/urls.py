from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:real_type>/<str:real_id>/', views.detail, name='detail'),
]
