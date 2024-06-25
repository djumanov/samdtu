from rest_framework import serializers
from .models import MenuItem, SubMenuItem


class SubMenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubMenuItem
        fields = ['id', 'title', 'url', 'menu_item']


class MenuItemSerializer(serializers.ModelSerializer):
    submenus = SubMenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'url', 'submenus']
