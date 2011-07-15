#from django.conf.urls.defaults import patterns, include, url
import os.path
from django.conf.urls.defaults import *
from bookmarks.views import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
from bookmarks.feeds import *

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
site_media = os.path.join(
	os.path.dirname(__file__), 'site_media'
)

# Make sure you add the feeds dict before the urlpatterns object.
feeds = {
	'recent': RecentBookmarks,
	'user' : UserBookmarks
}


urlpatterns = patterns('',
	#Feeds
	(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', 
						{'feed_dict': feeds}),
	
	#Admin interface
	(r'^admin/', include(admin.site.urls)),
	
	#Comments
	(r'^comments/', include('django.contrib.comments.urls')),

	#Ajax
	(r'^ajax/tag/autocomplete/$', ajax_tag_autocomplete),

	#Browsing
	(r'^$', main_page),
	(r'^user/(\w+)/$', user_page),
	(r'^tag/([^\s]+)/$', tag_page),
	(r'^tag/$', tag_cloud_page),
	(r'^search/$', search_page),
	(r'^popular/$', popular_page),
	(r'^bookmark/(\d+)/$', bookmark_page),

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
	(r'^vote/$', bookmark_vote_page),
)
