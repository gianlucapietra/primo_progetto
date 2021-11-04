from django.urls import path
from django.urls.resolvers import URLPattern
from prima_app.views import homepage
from prima_app.views import welcome
from prima_app.views import lista
from prima_app.views import ChiSiamo
from prima_app.views import index
from prima_app.views import variabili

app_name="prima_app"
urlpatterns=[
    path('homepage',homepage,name='homepage'),
    path('welcome',welcome,name='welcome'),
    path('lista',lista,name='lista'),
    path('ChiSiamo',ChiSiamo,name='ChiSiamo'),
    path('variabili',variabili,name='variabili'),
    path('',index,name='index'),
]