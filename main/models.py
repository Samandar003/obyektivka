from django.db import models

# Create your models here.

class Intro(models.Model):
    full_name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='pictures')
    date_birth = models.DateField()
    nationality = models.CharField(max_length=200)
    place_birth = models.CharField(max_length=100)
    partiyaviyligi = models.CharField(max_length=100)
    malumoti = models.CharField(max_length=100)
    malumoti_boyicha_mutaxasisligi = models.CharField(max_length=100)
    ilmiy_darajasi = models.CharField(max_length=100)
    qaysi_chet_tillarini_biladi = models.CharField(max_length=100)
    tamomlagan_maktab = models.CharField(max_length=100)
    ilmiy_unvoni = models.CharField(max_length=100)
    davlat_mukofotlari_tqadirlangan = models.CharField(max_length=100)
    mehnat_faoliyati = models.CharField(max_length=1000)
    saylov_azosi = models.CharField(max_length=200)
    
    qarindoshligi_1 = models.CharField(max_length=200)
    full_name_1 = models.CharField(max_length=200)
    tugilgan_yili_joyi_1 = models.CharField(max_length=200)
    ish_joyi_1 = models.CharField(max_length=200)
    turar_joyi_1 = models.CharField(max_length=200)
    
    qarindoshligi_2 = models.CharField(max_length=200)
    full_name_2 = models.CharField(max_length=200)
    tugilgan_yili_joyi_2 = models.CharField(max_length=200)
    ish_joyi_2 = models.CharField(max_length=200)
    turar_joyi_2 = models.CharField(max_length=200)
    
    qarindoshligi_3 = models.CharField(max_length=200)
    full_name_3 = models.CharField(max_length=200)
    tugilgan_yili_joyi_3 = models.CharField(max_length=200)
    ish_joyi_3 = models.CharField(max_length=200)
    turar_joyi_3 = models.CharField(max_length=200)
    
    qarindoshligi_4 = models.CharField(max_length=200)
    full_name_4 = models.CharField(max_length=200)
    tugilgan_yili_joyi_4 = models.CharField(max_length=200)
    ish_joyi_4 = models.CharField(max_length=200)
    turar_joyi_4 = models.CharField(max_length=200)
    
    qarindoshligi_5 = models.CharField(max_length=200, blank=True, null=True)
    full_name_5 = models.CharField(max_length=200, blank=True, null=True)
    tugilgan_yili_joyi_5 = models.CharField(max_length=200, blank=True, null=True)
    ish_joyi_5 = models.CharField(max_length=200, blank=True, null=True)
    turar_joyi_5 = models.CharField(max_length=200, blank=True, null=True)
    
    qarindoshligi_6 = models.CharField(max_length=200, blank=True, null=True)
    full_name_6 = models.CharField(max_length=200, blank=True, null=True)
    tugilgan_yili_joyi_6 = models.CharField(max_length=200, blank=True, null=True)
    ish_joyi_6 = models.CharField(max_length=200, blank=True, null=True)
    turar_joyi_6 = models.CharField(max_length=200, blank=True, null=True)
        
    def __str__(self):
        return self.full_name
    
class OutFile(models.Model):
    file = models.FileField(upload_to='out_files')
    
    