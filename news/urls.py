from django.urls import path
from django.urls.resolvers import URLPattern
from news.views import home, ArticoloDetailViewCB, GiornalistaDetailViewCB,GiornalistaListView,ArticoloListViewCB
app_name='news'


urlpatterns=[
    path('',home,name="homeview"),
   # path("articoli/<int:pk>",articoloDetailView,name="articolo_detail")
   path("articoli/<int:pk>", ArticoloDetailViewCB.as_view() ,name="articolo_detail"),
    path("lista_articoli/", ArticoloListViewCB.as_view() ,name="lista_articoli"),
    path("giornalisti/<int:pk>", GiornalistaDetailViewCB.as_view() ,name="giornalista_detail"),
    path("lista_giornalisti/", GiornalistaListView.as_view() ,name="lista_giornalisti"),
]
