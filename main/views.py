from django.shortcuts import render
from .serializers import *
from .models import Intro
from rest_framework import views
from rest_framework.views import APIView
from rest_framework.response import Response
from . import utils

class Hello(APIView):
    def get(self, request):
        return Response({'ms':"Hello"})

dic = {'date_birth':'27.04.2005', 
       'millati':'ozbek', 
       'place_birth':'Сурхондарйо вилояти', 
       'partiyaviyligi':'partiyasiz', 
       'malumoti':'orta',
    'malumoti_boyicha_mutaxasisligi':'', 
    'ilmiy_darajasi':'ўрта',
    'qaysi_chet_tillarini_biladi':'Инглиз тили',
    'tamomlagan_maktab':'14-ўрта мактаб',
    'ilmiy_unvoni':'Йўқ',
    'davlat_mukofotlari_tqadirlangan':'ИЕЛТС 5.5',
    'mehnat_faoliyati':'yoq'
    # 'saylov_azosi':'йўқ'
}


class IntroductionOby(APIView):
    def post(self, request):
        serializer = IntroductionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            intro1 = Intro.objects.get(id=serializer.data.get('id'))
            first_table_first_col_items = utils.first_table__first_col_key(serializer.data)
            second_table_first_col_items = utils.all_qarindoshlari(serializer.data)
            output = utils.intro_oby(intro1.full_name, intro1.picture, dic=first_table_first_col_items, qarindoshlari_keys=second_table_first_col_items)
            serializer = OutputFileSerializer(data=output)
            if serializer.is_valid():
                return Response(serializer.data)
        return Response({'ms':"pizdes"})  
    
          
          