from rest_framework import serializers
from .models import *

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields=('id','vName','price')

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Inventory
        fields=('id','vName','left')

class EntrySerializer(serializers.ModelSerializer):
    itemName=serializers.CharField(source='item.vName')
    class Meta:
        model=Entry
        fields=('itemName','qty','date')