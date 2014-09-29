from .models import Author,Comment,Post
from .serializers import PostSerializer

from django.http import Http404


from rest_framework.views import APIView
from rest_framework.response import Response

class PostList(APIView):
	"""
	Returns a list of all **published** posts
	"""
	def get(self,request,format=None):
		posts=Post.objects.all()
		serialized_posts=PostSerializer(posts,many=True)
		return Response(serialized_posts.data)

class PostDetail(APIView):
	"""
	Returns detail view of the post
	"""
	def get_object(self,pk):
		try:
			return Post.objects.get(pk=pk)
		except Post.DoesNotExist:
			raise Http404

	def get(self,request,pk,format=None):
		post=self.get_object(pk)
		serialized_post=PostSerializer(post)
		return Response(serialized_post.data)