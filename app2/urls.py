from django.urls import path

from app2.views import *

app_name='app2'

urlpatterns=[

    path('sample2/',sample2,name='sample2'),
]