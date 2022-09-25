from django.urls import path
from . import views


urlpatterns = [
    path('', views.Hello.as_view()),
    path('intro/', views.IntroductionOby.as_view()),
    # path('second/', views.ObyMidAPIView.as_view()),
]

