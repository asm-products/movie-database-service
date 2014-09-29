from django.db import models
from djangotoolbox.fields import ListField
# Create your models here.

from .forms import GenreListField

class GenreField(ListField):
    def formfield(self, **kwargs):
        return models.Field.formfield(self, GenreListField, **kwargs)

class Person(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	birth_date = models.DateField()
	def __unicode__(self):
		return "%s %s" %( self.first_name, self.last_name )

class Movie(models.Model):
	title = models.CharField(max_length=255)
	synopsis = models.TextField()
	classification = models.CharField(max_length=10)
	genres = GenreField()

	def __unicode__(self):
		return self.title