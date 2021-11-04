from django.shortcuts import render

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