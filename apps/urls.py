from django.urls import path

from apps import views
from apps.views import CategoryListAPIView, ProductCreateListAPIView, UserListAPIView

urlpatterns = [
    path('category', CategoryListAPIView.as_view(), name='category-list'),
    path('product', ProductCreateListAPIView.as_view(), name='product'),
    path('user', UserListAPIView.as_view(), name='users'),


]
