#from django.conf.urls.defaults import patterns, include, url
import os.path
from django.conf.urls.defaults import *
from bookmarks.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
site_media = os.path.join(
	os.path.dirname(__file__), 'site_media'
)

urlpatterns = patterns('',

	(r'^$', main_page),
	(r'^user/(\w+)/$', user_page),
	(r'^login/$', 'django.contrib.auth.views.login'),
	(r'^logout/$', logout_page),
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
		{ 'document_root': site_media }),
)
