from django.db import models
from djangotoolbox.fields import ListField
import datetime
from tinymce.models import HTMLField
from .forms import GenreListField


YEAR_CHOICES = []
for r in range(1700, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

MPAA_RATING= (
	('A','A'),
	('G','G'),
	('NC-17','NC-17'),
	('NR','NR'),
	('PG','PG'),
	('PG-13','PG-13'),
	('R','R'),
	('TV-Y','TV-Y'),
	('TV-Y7','TV-Y7'),
	('TV-Y7-FV','TV-Y7-FV'),
	('TV-G','TV-G'),
	('TV-PG','TV-PG'),
	('TV-14','TV-14'),
	('TV-MA','TV-MA'),
	('U','U'),
	('U/A','U/A'),
	('UR','UR'),
	('UNRATED','UNRATED'),
	
	)
GENRE = (
	('action','Action'),
	('adventure','Adventure'),
	('animation','Animation'),
	('biography','Biography'),
	('comedy','Comedy'),
	)
LANGUAGE = (
	('bhojpuri','Bhojpuri'),
	('english','English'),
	('hindi','Hindi'),
	('italian','Italian'),
	('japanese','Japanese'),
	('nepali','Nepali'),
	('tamil','Tamil'),
	('telugu','Telugu'),
	('tharu','Tharu'),
	)
class GenreField(ListField):
    def formfield(self, **kwargs):
        return models.Field.formfield(self, GenreListField, **kwargs)

class Person(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255,blank=True,null=True)
	birth_date = models.DateField(blank=True,null=True)
	bio = HTMLField(blank=True,null=True)

	def __unicode__(self):
		return "%s %s" %( self.first_name, self.last_name )

class Movie(models.Model):
	title = models.CharField(max_length=255)
	synopsis = HTMLField()
	story = HTMLField()
	classification = models.CharField(max_length=8, choices=MPAA_RATING)	
	language = models.CharField(max_length=255,choices=LANGUAGE)
	genres = GenreField()


	def __unicode__(self):
		return self.title

class ProductionHouse(models.Model):
	name = models.CharField(max_length=255)	
	headquarter = models.CharField(max_length=255)
	website = models.URLField()
	year = models.IntegerField(max_length=5,choices=YEAR_CHOICES,blank=True,null=True)
	founders = models.ManyToManyField(Person,related_name='productionhouse_founder')
	chairman = models.ManyToManyField(Person,related_name='productionhouse_chairman')
	ceo = models.ManyToManyField(Person,related_name='productionhouse_ceo')
	key_people= models.ManyToManyField(Person,related_name='productionhouse_keypeople')

	def __unicode__(self):
		return self.name