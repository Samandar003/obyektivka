from django.contrib import admin
from .models import Intro, OutFile


admin.site.register([Intro, OutFile])
