from django.urls import path
from .views import *

urlpatterns = [
    path('addUser/', Record.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('verify/<token>', EmailVerify.as_view(), name="email_verify"),
    path('address/', ShippingAddressView.as_view(), name='add_address'),
    path('address_detail/<int:pk>', ShippingAddressDetailView.as_view(), name='detail_address'),
    path('userinfo/<int:pk>', UserInformationView.as_view(), name='user_information_change'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('like/', UserFavoritesView.as_view(), name='like_user_to_product'),
    path('like_del/<int:pk>', UserFavoritesDeleteView.as_view(), name='user_favorites_delete'),
]

