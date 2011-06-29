#from django.conf.urls.defaults import patterns, include, url
import os.path
from django.conf.urls.defaults import *
from bookmarks.views import *
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
site_media = os.path.join(
	os.path.dirname(__file__), 'site_media'
)

urlpatterns = patterns('',

	#Browsing
	(r'^$', main_page),
	(r'^user/(\w+)/$', user_page),
	(r'^tag/([^\s]+)/$', tag_page),
	(r'^tag/$', tag_cloud_page),

	#Session management
	(r'^login/$', 'django.contrib.auth.views.login'),
	(r'^logout/$', logout_page),
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
		{ 'document_root': site_media }),
	(r'^register/$', register_page),
	(r'^register/success/$', direct_to_template,
		{ 'template': 'registration/register_success.html' }),
	
	#Account management
	(r'^save/$', bookmark_save_page),
)
