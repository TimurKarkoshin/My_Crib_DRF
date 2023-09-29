from django.urls import path, include
from .views import SmartphoneAPIView
from .views import SmartphoneAPIList, SmartphoneAPIUpdate, SmartphoneAPIDestroy
from .views import SmartphoneAPIDetailView
from .views import SmartphoneAPIViewSet
from rest_framework.routers import SimpleRouter, DefaultRouter

router = DefaultRouter()
router.register(r'api', SmartphoneAPIViewSet, basename="api")


app_name = 'smartphones'

urlpatterns = [
    path("", include(router.urls)),
    path("api/", SmartphoneAPIViewSet.as_view({'get': 'list'}), name="smartphone-api"),
    path("api/update/<int:pk>", SmartphoneAPIViewSet.as_view({'put': 'update'}), name="smartphone-api-update"),
    path("api/<int:pk>", SmartphoneAPIDetailView.as_view(), name="smartphone-api"),
    path("api/", SmartphoneAPIList.as_view(), name="smartphone-api"),
    path("api/update/<int:pk>", SmartphoneAPIUpdate.as_view(), name="smartphone-api-update"),
    path("api/delete/<int:pk>", SmartphoneAPIDestroy.as_view(), name="smartphone-api-delete"),
    path("api/", SmartphoneAPIView.as_view(), name="smartphone-api"),
    path("api/<int:pk>", SmartphoneAPIView.as_view(), name="smartphone-api-pk")
]
