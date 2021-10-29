from django.urls import path
from django.urls.resolvers import URLPattern
from prima_app.views import homepage
from prima_app.views import welcome
from prima_app.views import lista
from prima_app.views import ChiSiamo

app_name="prima_app"
urlpatterns=[
    path('',homepage,name='homepage'),
    path('welcome',welcome,name='welcome'),
    path('lista',lista,name='name'),
    path('ChiSiamo',ChiSiamo,name='ChiSiamo'),
]