from django.urls import path
from seconda_app.views import es_if
from seconda_app.views import es_ifelse
from seconda_app.views import es_for 
app_name="seconda_app"
urlpatterns =[
    path('es_if',es_if,name="es_if"),
    path('es_ifelse',es_ifelse,name="es_ifelse"),
    path('es_for',es_for,name="es_for"),
]
