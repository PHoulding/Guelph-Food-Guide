# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.http import HttpResponseRedirect, HttpResponse
from .models import Resource, onCampusResource
# Register your models here.
class resource_admin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		obj.save()

class onCampusResource_admin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		obj.save()

admin.site.register(Resource, resource_admin)
admin.site.register(onCampusResource, onCampusResource_admin)