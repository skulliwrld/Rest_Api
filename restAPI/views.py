from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from Realapp.models import stock
from Realapp.serializer import stockserializer
from rest_framework.permissions import IsAuthenticated

class RealView(APIView):
    permission_classes =(IsAuthenticated, )



    def get(self, request,*args,**kwargs):
        qs= stock.objects.all()
        serializer=stockserializer(qs,many=True)
        return Response(serializer.data)

    def post(self, request,*args,**kwargs):
        serializer=stockserializer(data= request.data)

        if serializer .is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def update(self,request,pk):
        qs = stock.objects.get(pk=pk)
        serializer = stockserializer(instance=qs,data=request.data)

        if serializer .is_valid():
            serializer.save()
            return Response(serializer.data)
        return (serializer.errors)
    
    def delete(self,request,pk):
        qs = stock.objects.get(pk=pk)
        serializer=stockserializer(qs)
        del serializer
        serializer.save()
        
        
        