from django.db import models

# Create your models here.
class Inventory(models.Model):
    vName=models.CharField(max_length=40,null=True,blank=False)
    price=models.PositiveIntegerField()
    left = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=10,default='units')
    threshold = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.vName

class Item(models.Model):
    vName=models.CharField(max_length=40,null=True,blank=False)
    price=models.PositiveIntegerField()
    ingredients=models.ManyToManyField(Inventory,through='Ingredient')

    def __str__(self):
        return self.vName

class Ingredient(models.Model):
    inventory=models.ForeignKey(Inventory,on_delete=models.CASCADE)
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    amount=models.FloatField()
    unit=models.CharField(max_length=10)

    def __str__(self):
        return self.item.vName+" NEEDS "+self.inventory.vName



class Entry(models.Model):
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    qty=models.PositiveIntegerField()
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.item)+" | "+str(self.qty)+"  |  "+str(self.date)

class Notification(models.Model):
    date=models.DateField(auto_now_add=True)
    totalSale=models.PositiveIntegerField(default=0)
    smsSent=models.BooleanField(default=False)