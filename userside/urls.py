from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('vehicles', views.Vehicle)
router.register('shops', views.Shop)


urlpatterns = [
    path('', include(router.urls)),
]