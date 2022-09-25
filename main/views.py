from django.shortcuts import render
from rest_framework import status
from main import obyektivka
from .serializers import *
from .models import Intro
from rest_framework import views
from rest_framework.views import APIView
from rest_framework.response import Response


class Hello(APIView):
    def get(self, request):
        return Response({'ms':"Hello"})

class IntroductionOby(APIView):
    def post(self, request):
        serializer = IntroductionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            intro1 = Intro.objects.get(id=serializer.data.get('id'))
            first_table_first_col_items = obyektivka.first_table__first_col_key(serializer.data)
            second_table_first_col_items = obyektivka.all_qarindoshlari(serializer.data)
            output = obyektivka.intro_oby(intro1.full_name, intro1.picture, dic=first_table_first_col_items, qarindoshlari_keys=second_table_first_col_items)
            serializer = OutputFileSerializer(data=output)
            if serializer.is_valid():
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
          
          