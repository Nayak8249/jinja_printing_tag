from django.shortcuts import render

def jinja_print(request):
    d={'name':'BIBHUTI','age':25}
    return render(request,'jinja_print.html',d)

