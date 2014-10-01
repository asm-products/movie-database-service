from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from blog import api

import views

urlpatterns = patterns(
	'',
 	#API
    url(r'^posts/$',api.PostList.as_view()),    
    url(r'^posts/(?P<pk>[0-9a-zA-Z]+)/$',api.PostDetail.as_view()),    

)
