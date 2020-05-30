from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request, 'index.html',{'name':'Ashutosh'})

def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    
    res = val1+val2 

    return render(request, 'results.html',{'result':res})

# def results(request):
    
#     val1 = request.GET['num1']
#     val2 = request.GET['num2']
    
#     res = val1+val2

#     return render(request, ' results.html',{'result':res})