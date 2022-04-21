from django.db import router
from django.urls import path, include
from rest_framework import routers

from .views import WordViewSet


router = routers.DefaultRouter()
router.register('word', WordViewSet)

urlpatterns = [
    path('', include(router.urls))
]