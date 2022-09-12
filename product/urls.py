from django.urls import path
from .views import *

urlpatterns = [
    path('add/', ProductView.as_view(), name='add_product'),
    path('list/<int:page>', ProductListView.as_view(), name='product_list'),
    path('ud/<int:pk>', ProductUDView.as_view(), name='update_delete_product'),
    path('category/', CategoryView.as_view(), name='add_category'),
    path('category_detail/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
    path('type/', TypeView.as_view(), name='add_type'),
    path('type_detail/<int:pk>', TypeDetailView.as_view(), name='type_detail'),
]
