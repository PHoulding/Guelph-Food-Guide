# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
@python_2_unicode_compatible
class Resource(models.Model):
	price_point = (('$','$'),('$$','$$'),('$$$','$$$'))
	restaurantName = models.CharField(max_length = 50)
	restaurantLocation = models.CharField(max_length = 50)
	restaurantMenu = models.URLField(max_length = 500)
	dietaryRestrictions = models.CharField(max_length = 50, default="n/a")
	pricePoint = models.CharField(max_length=3, choices=price_point, default="$$")
	def __str__(self):
		return self.restaurantName+", "+self.restaurantLocation+", "+self.restaurantMenu

@python_2_unicode_compatible
class onCampusResource(models.Model):
	buildingName = models.CharField(max_length = 50)
	list_of_resources = models.ForeignKey(Resource, on_delete=models.CASCADE)
	def __str__(self):
		return self.buildingName+", "+self.list_of_resources
