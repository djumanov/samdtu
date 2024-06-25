from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, SubMenuItemViewSet


router = DefaultRouter()
router.register(r'menus', MenuItemViewSet)
router.register(r'submenus', SubMenuItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
