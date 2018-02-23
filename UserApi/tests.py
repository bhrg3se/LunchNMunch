from django.test import TestCase
from .models import *
# Create your tests here.
class TestApis(TestCase):
    def setUp(self):
        """Define the test client and other test variables."""
        #Define items
        momo=Item.objects.create(vName='MoMo',price=100)
        bara=Item.objects.create(vName='Bara',price=50)
        choila=Item.objects.create(vName='Choila',price=80)

        #Define Inventories
        salt=Inventory.objects.create(vName='Salt',price=20)
        chilly=Inventory.objects.create(vName='Chilly',price=10)
        oil=Inventory.objects.create(vName='Oil',price=100)

        potato=Inventory.objects.create(vName='Potato',price=100)
        maida=Inventory.objects.create(vName='maida',price=150)
        chamal=Inventory.objects.create(vName='Chamal',price=120)

        #Define Ingredients
        i=Ingredient.objects.create(inventory=maida,item=momo,amount=100,unit="mg")
        i.save()
        i = Ingredient.objects.create(inventory=salt, item=momo, amount=5, unit="mg")
        i.save()
        i = Ingredient.objects.create(inventory=chamal, item=bara, amount=100, unit="mg")
        i.save()
        i = Ingredient.objects.create(inventory=chilly, item=bara, amount=5, unit="mg")
        i.save()



    def test_add_item(self):
        print(Item.objects.all().values())
        print(Item.objects.get(vName='MoMo').ingredient_set.all().values())