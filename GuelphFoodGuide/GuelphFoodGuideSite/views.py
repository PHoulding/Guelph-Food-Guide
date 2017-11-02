# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
import re

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
	return render(request, 'GuelphFoodGuide/DietaryInfo.html', context)

def menu(request, menuName=None):
	instance = get_object_or_404(models.Resource, restaurantName=menuName)
	temp = instance.restaurantMenu
	temp = temp.split("\r\n")
	menuItems=[]
	for line in temp:
		menuItems.append(line)
	#context={
	#	"restaurantName":instance.restaurantName,
	#	"menu":instance.restaurantMenu

	#}
	return render(request, 'GuelphFoodGuide/menu.html', {'restaurantName':instance.restaurantName,'menuItems':menuItems})