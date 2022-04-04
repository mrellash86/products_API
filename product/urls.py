from django.urls import path
from . import views

urlpatterns = [
    path('', views.productList, name='product-list'),
    path('product/<str:pk>/', views.productDetails, name='product'),

    path('api/product', views.apiProduct),
    path('api/details/<str:pk>/', views.apiProductDetails),
    path('api/create', views.apiCreateProduct),
    path('api/update/<str:pk>/', views.apiUpdateProduct),
    path('api/delete/<str:pk>/', views.apiDeleteProduct),
]
