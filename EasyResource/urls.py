from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from django.urls import path

from shoe import views as shoe_view

router = routers.DefaultRouter()
router.register(r'shoe', shoe_view.ShoeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^csv_import/', shoe_view.CsvView.as_view())
]