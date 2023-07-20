from django.urls.conf import include, path
from rest_framework.routers import DefaultRouter
from app_one.views import PersonViewSet

router = DefaultRouter()
router.register("person", PersonViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
