from django.conf.urls import patterns, include, url
from django.contrib import admin
from mongoadmin import site
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User

admin.autodiscover()

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'anee.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
	url(r'^api/', include('blog.urls')), #blog api
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
)
urlpatterns=format_suffix_patterns(urlpatterns)