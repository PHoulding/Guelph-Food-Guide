from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index,name="index"),
	url(r'NutritionGuide',views.NutritionGuide,name="NutritionGuide Guide"),
	url(r'Resources',views.resources,name="Resources"),
	url(r'FoodMap',views.foodMap,name="Food Map"),
	url(r'DietaryInfo',views.dietaryInfo,name="DietaryInfo"),
	url(r'menu/(?P<menuName>(\w*\W*)+)',views.menu, name="Menu")
]
