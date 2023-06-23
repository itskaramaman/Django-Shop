from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='home'),
    path('products/<int:id>/', views.product_detail, name='home'),
     path('collections/<int:id>/', views.collection_detail, name='collection-detail')
]