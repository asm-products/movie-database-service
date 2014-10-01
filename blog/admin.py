from django.contrib import admin
from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType

from blog.models import Author,Comment,Post
# Register your models here.

def tags(instance):
	return ', '.join(instance.tags)

class AuthorAdmin(admin.ModelAdmin):
	list_display=['name','email']

class CommentAdmin(admin.ModelAdmin):
	list_display=['author','text']

class PostAdmin(admin.ModelAdmin):
	list_display=['title',tags,'author']	

admin.site.register(Author,AuthorAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Post,PostAdmin)
