from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item,Entry,Ingredient,Inventory,Notification
from rest_framework import permissions
from .serializers import ItemSerializer,InventorySerializer,EntrySerializer
import datetime

class ItemList(APIView):
    #permission_classes =permissions.AllowAny
    def get(self,request):
        items=Item.objects.all()
        serializer=ItemSerializer(items,many=True)
        return Response(serializer.data)

class AddEntry(APIView):
    def get(self,request):
        try:
            id = request.query_params['id']
            qty = request.query_params['qty']
            entry = Entry(item_id=id, qty=qty)
            ingredients= Item.objects.get(id=id).ingredient_set.all()
            for ing in ingredients:
                amt=ing.amount
                ing.inventory.left -= amt
                ing.inventory.save()
            entry.save()
            return Response('success')
        except Exception as e:
            print(e)
            return Response('error')

class CheckInventory(APIView):
    def get(self,request):
        l=[]
        inventories=Inventory.objects.all()
        for inventory in inventories:
            if(inventory.left<inventory.threshold):
                l.append(inventory)
        s=InventorySerializer(l,many=True)
        return Response(s.data)

class CheckSale(APIView):
    def get(self,request):
        day=int(request.query_params['day'])
        month=int(request.query_params['month'])
        year=int(request.query_params['year'])
        try:
            todayEntry=Entry.objects.filter(date__day=day,date__month=month,date__year=year)
        except Entry.DoesNotExist:
            todayEntry=None
            pass
        return Response(EntrySerializer(todayEntry,many=True).data)

class SmsNotification(APIView):
    sales=0
    def get(self,request):
        sent=request.query_params['sent']
        today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        try:
            notif=Notification.objects.get(date__range=(today_min,today_max))
            self.sales=notif.totalSale
        except Notification.DoesNotExist:
            try:
                todayEntry = Entry.objects.filter(date__range=(today_min, today_max))
            except Entry.DoesNotExist:
                todayEntry = None
            for i in todayEntry.all():
                self.sales = self.sales + (i.qty) * (i.item.price)
            notif=Notification(smsSent=False,totalSale=self.sales)
            notif.save()


        if(sent=='true'):
            notif.smsSent=True
            notif.save()
            return Response(0)
        elif(notif.smsSent==False):
            return Response(self.sales)
        else:
            return Response(-1)  #already sent







