from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from person.models import Person
from person.serializers import Sportserializers




class Listsports(APIView):
    def get(self,request):
        list1 = Person.objects.all().values()
        return Response({'famous': Sportserializers(list1, many=True).data})
    def post(self,requests):
        posts = Person.objects.create(
            name=requests.data["name"],
            cat_id=requests.data["cat_id"],
        )
        return Response({"posts": Sportserializers(posts).data})







# class Listsports(generics.ListAPIView):
#     queryset = Person.objects.all()
#     serializer_class = Sportserializers
