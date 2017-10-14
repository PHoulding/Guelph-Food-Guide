# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def index(request):
	context = {}
	return render(request, 'GuelphFoodGuide/index.html',context)

def NutritionGuide(request):
	context={}
	return render(request, 'GuelphFoodGuide/NutritionGuide.html',context)

def resources(request):
	resources = models.Resource.objects.all()
	return render(request, 'GuelphFoodGuide/Resources.html',{'resources':resources})

def foodMap(request):
	context={}
	return render(request, 'GuelphFoodGuide/FoodMap.html',context)

def dietaryInfo(request):
	context={}
	return render(request, 'GuelphFoodGuide/DietaryInfo.html')