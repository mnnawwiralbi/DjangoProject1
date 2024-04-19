from django.urls import path, include
from rest_framework.routers import DefaultRouter
from APIdata.Data1.MyModelsViewSet import MyModelViewSets

router = DefaultRouter()
router.register('member2', MyModelViewSets)

urlpatterns = [
   path('', include(router.urls)),
]
