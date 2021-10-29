from django.urls import path
from django.urls.resolvers import URLPattern
from prima_app.views import homepage

app_name="prima_app"
urlpatterns=[
    path('',homepage,name='homepage'),
]