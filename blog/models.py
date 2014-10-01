__author__ = 'opnchaudhary'

from django.db import models
from djangotoolbox.fields import ListField,EmbeddedModelField

from .forms import TagListField,AuthorListField

class TagField(ListField):
    def formfield(self, **kwargs):
        return models.Field.formfield(self, TagListField, **kwargs)

class EmbedAuthorOverrideField(EmbeddedModelField):
    def formfield(self, **kwargs):
        return models.Field.formfield(self, AuthorListField, **kwargs)

class Author(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField()

	def __unicode__(self):
		return self.name

class Comment(models.Model):
	post = models.ForeignKey('Post')
	author = EmbedAuthorOverrideField('Author')
	text = models.TextField()

	def __unicode__(self):
		return self.text


class Post(models.Model):
	author = EmbedAuthorOverrideField('Author')
	title = models.CharField(max_length=255)
	text = models.TextField()
	tags = TagField()	
	#comments = ListField(EmbeddedModelField('Comment'))
	updated_on = models.DateTimeField(auto_now_add=True,null=True)

	def __unicode__(self):
		return self.title



