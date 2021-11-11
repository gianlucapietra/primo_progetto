from django.shortcuts import render
import datetime
# Create your views here.
def es_if(request):
    context= {
        'var1': 200,
        'var2': 200,
        'var3': 300,
    }
    return render(request,"es_if.html",context)
def es_ifelse(request):
    context= {
        'var1': 100,
        'var2': 100.0,
        'var3': 100.50,
    }
    return render(request,"es_ifelse.html",context)
def es_for(request):
    context= {
        'list1':[1,datetime.date(2021,11,11), 'non ti arrendere'],
        'list2':[1,datetime.date(2021,11,11), 'non ti arrendere'],
    }
    return render(request, "es_for.html", context)
    
    