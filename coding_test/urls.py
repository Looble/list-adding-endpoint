from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from coding_test.number_sum.views import TotalViewSet

# Use Django Rest Framework's router module to quickly generate the required URL
router = routers.DefaultRouter()
router.register(r'total', TotalViewSet, 'Total')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
