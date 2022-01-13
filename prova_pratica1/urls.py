from django.urls import path
from django.urls.resolvers import URLPattern
from prova_pratica1.views import view_b
from prova_pratica1.views import view_c

app_name="prova_pratica1"
urlpatterns=[
    path('view_b',view_b,name='view_b'),
    path('view_c',view_c,name='view_c')
]