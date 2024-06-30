from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from person import serializers
from person.models import Person
from person.serializers import Sportserializers




class Listsports(APIView):
    def get(self,request, pk):
        if not pk:
            return Response({"get": "Method GET not allowed!"})

        try:
            instanse = Person.objects.get(pk=pk)
        except:
            return Response({"famous": "Object not found!!!"})
        serializers = Sportserializers(instanse)
        return Response({"get": serializers.data})

    def post(self, requests):
        serializers = Sportserializers(data=requests.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()

        return Response({"posts": serializers.data})
    def put(self, requests, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"post": "Method PUT not allowed!"})

        try:
            instance = Person.objects.get(pk=pk)
        except:
            return Response({"post": "Object not found!"})

        serializers = Sportserializers(data=requests.data, instance=instance)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({"post": serializers.data})

    def patch(self, requests, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"post": "Method PUT not allowed!"})

        try:
            instance = Person.objects.get(pk=pk)
        except:
            return Response({"post": "Object not found!"})

        serializers = Sportserializers(data=requests.data, instance=instance, partial=True)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({"post": serializers.data})

    def delete(self, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"post": "Method PUT not allowed!"})
        try:
            instance = Person.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({"post": "Object not found!"})

        return Response({"answer": f"Deleted ID - {pk}"})
# class Listsports(generics.ListAPIView):
#     queryset = Person.objects.all()
#     serializer_class = Sportserializers
