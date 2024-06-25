from rest_framework import viewsets
from .models import MenuItem, SubMenuItem
from .serializers import MenuItemSerializer, SubMenuItemSerializer


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SubMenuItemViewSet(viewsets.ModelViewSet):
    queryset = SubMenuItem.objects.all()
    serializer_class = SubMenuItemSerializer
