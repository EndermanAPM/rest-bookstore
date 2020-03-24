
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.bookshop import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('customers', views.CustomerAPI)
router.register('genres', views.GenreAPI)
router.register('books', views.BookAPI)
router.register('orders', views.OrderAPI)
router.register('orderbook', views.OrderBookQuantityAPI)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
