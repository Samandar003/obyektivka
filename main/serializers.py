from rest_framework import serializers

from main.models import Intro

class IntroductionSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=300)
    picture = serializers.FileField(
        max_length = 10000000,
        allow_empty_file = False,
        use_url = False,)
    
    date_birth = serializers.DateField()
    nationality = serializers.CharField()
    place_birth = serializers.CharField(max_length=100)
    partiyaviyligi = serializers.CharField(max_length=100)
    malumoti = serializers.CharField(max_length=100)
    malumoti_boyicha_mutaxasisligi = serializers.CharField(max_length=100)
    ilmiy_darajasi = serializers.CharField(max_length=100)
    qaysi_chet_tillarini_biladi = serializers.CharField(max_length=100)
    tamomlagan_maktab = serializers.CharField(max_length=100)
    ilmiy_unvoni = serializers.CharField(max_length=100)
    davlat_mukofotlari_tqadirlangan = serializers.CharField(max_length=100)
    mehnat_faoliyati = serializers.CharField(max_length=1000)
    saylov_azosi = serializers.CharField(max_length=200)
    
    qarindoshligi_1 = serializers.CharField(max_length=200)
    full_name_1 = serializers.CharField(max_length=200)
    tugilgan_yili_joyi_1 = serializers.CharField(max_length=200)
    ish_joyi_1 = serializers.CharField(max_length=200)
    turar_joyi_1 = serializers.CharField(max_length=200)
    
    qarindoshligi_2 = serializers.CharField(max_length=200)
    full_name_2 = serializers.CharField(max_length=200)
    tugilgan_yili_joyi_2 = serializers.CharField(max_length=200)
    ish_joyi_2 = serializers.CharField(max_length=200)
    turar_joyi_2 = serializers.CharField(max_length=200)
    
    qarindoshligi_3 = serializers.CharField(max_length=200)
    full_name_3 = serializers.CharField(max_length=200)
    tugilgan_yili_joyi_3 = serializers.CharField(max_length=200)
    ish_joyi_3 = serializers.CharField(max_length=200)
    turar_joyi_3 = serializers.CharField(max_length=200)
    
    qarindoshligi_4 = serializers.CharField(max_length=200)
    full_name_4 = serializers.CharField(max_length=200)
    tugilgan_yili_joyi_4 = serializers.CharField(max_length=200)
    ish_joyi_4 = serializers.CharField(max_length=200)
    turar_joyi_4 = serializers.CharField(max_length=200)
    
    qarindoshligi_5 = serializers.CharField(max_length=200, required=False)
    full_name_5 = serializers.CharField(max_length=200, required=False)
    tugilgan_yili_joyi_5 = serializers.CharField(max_length=200, required=False)
    ish_joyi_5 = serializers.CharField(max_length=200, required=False)
    turar_joyi_5 = serializers.CharField(max_length=200, required=False)
    
    qarindoshligi_6 = serializers.CharField(max_length=200, required=False)
    full_name_6 = serializers.CharField(max_length=200, required=False)
    tugilgan_yili_joyi_6 = serializers.CharField(max_length=200, required=False)
    ish_joyi_6 = serializers.CharField(max_length=200, required=False)
    turar_joyi_6 = serializers.CharField(max_length=200, required=False)
    
    
    def create(self, validated_data):
        full_name = validated_data.pop('full_name')
        picture = validated_data.pop('picture')
            
        return Intro.objects.create(
            full_name=full_name, picture=picture, date_birth=validated_data.pop('date_birth'),
            nationality=validated_data.pop('nationality'), place_birth=validated_data.pop('place_birth'),
            partiyaviyligi=validated_data.pop('partiyaviyligi'),
            malumoti=validated_data.pop('malumoti'), 
            malumoti_boyicha_mutaxasisligi = validated_data.pop('malumoti_boyicha_mutaxasisligi'),
            ilmiy_darajasi = validated_data.pop('ilmiy_darajasi'),
            qaysi_chet_tillarini_biladi = validated_data.pop('qaysi_chet_tillarini_biladi'),
            tamomlagan_maktab = validated_data.pop('tamomlagan_maktab'),
            ilmiy_unvoni = validated_data.pop('ilmiy_unvoni'),
            davlat_mukofotlari_tqadirlangan = validated_data.pop('davlat_mukofotlari_tqadirlangan'),
            mehnat_faoliyati = validated_data.pop('mehnat_faoliyati'),
            saylov_azosi = validated_data.pop('saylov_azosi'),
            
            qarindoshligi_1 = validated_data.pop('qarindoshligi_1'),
            full_name_1 = validated_data.pop('full_name_1'),
            tugilgan_yili_joyi_1 = validated_data.pop('tugilgan_yili_joyi_1'),
            ish_joyi_1 = validated_data.pop('ish_joyi_1'),
            turar_joyi_1 = validated_data.pop('turar_joyi_1'),
            
            qarindoshligi_2 = validated_data.pop('qarindoshligi_2'),
            full_name_2 = validated_data.pop('full_name_2'),
            tugilgan_yili_joyi_2 = validated_data.pop('tugilgan_yili_joyi_2'),
            ish_joyi_2 = validated_data.pop('ish_joyi_2'),
            turar_joyi_2 = validated_data.pop('turar_joyi_2'),
            
            qarindoshligi_3 = validated_data.pop('qarindoshligi_3'),
            full_name_3 = validated_data.pop('full_name_3'),
            tugilgan_yili_joyi_3 = validated_data.pop('tugilgan_yili_joyi_3'),
            ish_joyi_3 = validated_data.pop('ish_joyi_3'),
            turar_joyi_3 = validated_data.pop('turar_joyi_3'),
            
            qarindoshligi_4 = validated_data.pop('qarindoshligi_4'),
            full_name_4 = validated_data.pop('full_name_4'),
            tugilgan_yili_joyi_4 = validated_data.pop('tugilgan_yili_joyi_4'),
            ish_joyi_4 = validated_data.pop('ish_joyi_4'),
            turar_joyi_4 = validated_data.pop('turar_joyi_4'),
            
            qarindoshligi_5 = validated_data.pop('qarindoshligi_5', ''),
            full_name_5 = validated_data.pop('full_name_5', ''),
            tugilgan_yili_joyi_5 = validated_data.pop('tugilgan_yili_joyi_5', ''),
            ish_joyi_5 = validated_data.pop('ish_joyi_5', ''),
            turar_joyi_5 = validated_data.pop('turar_joyi_5', ''),
            
            qarindoshligi_6 = validated_data.pop('qarindoshligi_6', ''),
            full_name_6 = validated_data.pop('full_name_6', ''),
            tugilgan_yili_joyi_6 = validated_data.pop('tugilgan_yili_joyi_6', ''),
            ish_joyi_6 = validated_data.pop('ish_joyi_6', ''),
            turar_joyi_6 = validated_data.pop('turar_joyi_6', '')
            )

    class Meta:
        model = Intro
        fields = '__all__'


class OutputFileSerializer(serializers.Serializer):
    file = serializers.FileField(
        max_length = 10000000,
        allow_empty_file = False,
        use_url = False,
    )
    
    