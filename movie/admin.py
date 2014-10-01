from django.contrib import admin
from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from django import forms

from movie.models import Person,Movie,ProductionHouse


#class ProductionHouseForm(forms.ModelForm):
#	class Meta:		
		#model = ProductionHouse
		#exclue = ['founders','ceo','key_people','chairman']


def genres(instance):
	return ', '.join(instance.genres)

class PersonAdmin(admin.ModelAdmin):
	list_display =['first_name','last_name','birth_date']

class MovieAdmin(admin.ModelAdmin):
	list_display = ['title','classification','language',genres]
	list_filter = ['language','classification']

class ProductionHouseAdmin(admin.ModelAdmin):
#	form = ProductionHouseForm
	list_display = ['name','founders','year','headquarter']

admin.site.register(Person,PersonAdmin)
admin.site.register(Movie,MovieAdmin)
admin.site.register(ProductionHouse,ProductionHouseAdmin)
