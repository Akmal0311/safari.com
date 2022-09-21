from django.urls import path
from .views import *

urlpatterns = [
    path('product_add/', ProductView.as_view(), name='add_product'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='update_delete_product'),
    path('category/', CategoryView.as_view(), name='add_category'),
    path('category_detail/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
    path('type/', TypeView.as_view(), name='add_type'),
    path('type_detail/<int:pk>', TypeDetailView.as_view(), name='type_detail'),
]
