from django.contrib import admin
from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType

from movie.models import Person,Movie

def genres(instance):
	return ', '.join(instance.genres)

class PersonAdmin(admin.ModelAdmin):
	list_display =['first_name','last_name']

class MovieAdmin(admin.ModelAdmin):
	list_display = ['title',genres]

admin.site.register(Person,PersonAdmin)
admin.site.register(Movie,MovieAdmin)
