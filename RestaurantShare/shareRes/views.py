from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request) :
    #return HttpResponse('index')
    return render(request, 'shareRes/index.html')

def restaurantDetail(request) :
    #return HttpResponse("restaurantDetail")
    return render(request, 'shareRes/restaurantDetail')

def restaurantCreate(request) :
    # return HttpResponse("restaurantCreate")
    return render(request, 'shareRes/restaurantCreate.html')

def categoryCreate(request) :
    # return HttpResponse("categoryCreate")
    return render(request, 'shareRes/categoryCreate.html')