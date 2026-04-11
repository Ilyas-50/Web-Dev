from django.urls import path
from api import views

urlpatterns = [
    path('categories/', views.CategoryListAPIView.as_view()),
    path('categories/<int:pk>/', views.CategoryDetailAPIView.as_view()),
    path('categories/<int:id>/products/', views.CategoryProductsAPIView.as_view()),

    path('products/active/', views.ActiveProductListAPIView.as_view()),
    path('products/expensive/', views.ExpensiveProductListAPIView.as_view()),

    path('products/', views.ProductListAPIView.as_view()),
    path('products/<int:product_id>/', views.ProductDetailAPIView.as_view()),
]

# urlpatterns = [
#     path('categories/', views.category_list),
#     path('categories/<int:pk>/', views.category_detail),
#     path('categories/<int:id>/products/', views.category_products),

#     path('products/active/', views.active_products),
#     path('products/expensive/', views.expensive_products),

#     path('products/', views.products_list),
#     path('products/<int:product_id>/', views.product_detail),
# ]