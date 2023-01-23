from django.http import HttpResponse
from django.shortcuts import render
from .models import*

# Create your views here.
def hello(request):
    obj = News.objects.all()
    return render(request, 'index.html',{'result': obj })

# def about(request):
#     return HttpResponse("About Page")

# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res_add = x+y
#     res_sub = x-y
#     res_mult = x*y
#     res_div = x/y
#     return render(request, 'result.html',{'res_add':res_add, 'res_sub':res_sub,'res_mult':res_mult,'res_div':res_div})