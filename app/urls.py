from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.ProductHomeView.as_view(), name='home'),

    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),

    path('baseball/', views.baseball, name='baseball'),
    path('baseballdata/<slug:data>/', views.baseball, name='baseballdata'),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


