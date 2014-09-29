from .models import Author,Comment,Post
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model=Author
		fields=(
				'name',
				'email'
				)

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = (
			'id',
			'title',
			'text',
			'tags',
			'author'
			)