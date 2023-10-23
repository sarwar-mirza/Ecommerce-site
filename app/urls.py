from django.urls import path
from app import views

urlpatterns = [
    path('', views.ProductHomeView.as_view(), name='home'),
]