from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.ProductHomeView.as_view(), name='home'),

    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),

    path('baseball/', views.baseball, name='baseball'),
    path('baseballdata/<slug:data>/', views.baseball, name='baseballdata'),

    path('football/', views.football, name='football'),
    path('footballdata/<slug:data>/', views.football, name='footballdata'),

    path('cricket/', views.cricket, name='cricket'),
    path('cricketdata/<slug:data>/', views.cricket, name='cricketdata'),

    path('allproduct/', views.allproduct, name='allproduct'),

    

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


