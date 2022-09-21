from django.shortcuts import redirect
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .serializers import *
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.template import loader
from rest_framework.views import APIView
from product.models import *


class Record(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user = request.data

        users = User.objects.all()

        for i in range(len(users)):
            a = users[i]

            if a.username == user['username']:
                return Response(data="Bunday username ro'yxtdan o'tgan boshqa username kiriting", status=400)

            if a.email == user['email']:
                return Response(data="Bunday email ro'yxatdan o'tgan boshqa email kiriting", status=400)

        res = User.objects.create(
            username=user['username'],
            email=user['email'],
            avatar=user['avatar'],
            user_token=send_email_token(user['email'])
        )

        res.save()

        return Response(data={"message": "Tabriklaymiz siz ro'yxatdan o'tdingiz\naccountingizni tastiqlash uchun email pochtangizga kirib Confirm Account tugmasini bosing"})


class Login(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLoginSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


class Logout(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserLogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLogoutSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


class EmailVerify(APIView):
    def get(self, request, *args, **kwargs):
        token = kwargs["token"]
        try:
            user = User.objects.get(user_token=token)
            user.is_verified = True
            user.save()
            return Response(data="Sizning email pochtangiz tastiqlandi!", status=200)
        except:
            return Response(data="Sizning email pochtangiz tastiqlanmadi hatolik bor!", status=400)


class ShippingAddressView(generics.ListCreateAPIView):
    queryset = ShippingAddress
    serializer_class = ShippingAddressSerializer


class ShippingAddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShippingAddress
    serializer_class = ShippingAddressSerializer


class UserInformationView(generics.UpdateAPIView):
    queryset = User
    serializer_class = UserInformationSerializer


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User

    def get(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserFavoritesView(generics.CreateAPIView):
    queryset = UserFavorites
    serializer_class = UserFavoritesSerializer

    def post(self, request, *args, **kwargs):
        data = request.data

        user = User.objects.get(id=data['user'])
        product = Product.objects.get(id=data['product'])

        if not user:
            return Response(data='User topilmadi', status=status.HTTP_404_NOT_FOUND)
        if not product:
            return Response(data='Product toplimadi', status=status.HTTP_404_NOT_FOUND)

        product.like += 1

        product.save()

        UserFavorites.objects.create(
            user=user,
            product=product
        )

        return Response(data='successfully', status=status.HTTP_200_OK)


class UserFavoritesDeleteView(APIView):
    queryset = UserFavorites
    serializer_class = UserFavoritesSerializer

    def delete(self, request, pk):
        like = UserFavorites.objects.get(pk=pk)

        if not like:
            return Response(data="like topilmadi", status=status.HTTP_404_NOT_FOUND)

        product = Product.objects.get(id=like.product.id)

        product.like -= 1

        product.save()

        like.delete()

        return Response(data='successfully', status=status.HTTP_200_OK)


def index(request):
    return redirect('/api/login')


def send_email_token(email):
    token = get_random_string(length=20)
    html_message = loader.render_to_string(
        "email.html", {"token": token}
    )

    send_mail(
        "Safari",
        None,
        "shamshod2426298@mail.ru",
        [email],
        fail_silently=False,
        html_message=html_message,
    )
    return token
