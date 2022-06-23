from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('aboutus/',views.aboutUs),
    path('aboutyou/',views.aboutYou),
    path('privacypolicy/',views.privacyPolicy),
    path('termsandcondition/',views.termsAndCondition),
]