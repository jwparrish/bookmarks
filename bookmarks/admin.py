from django.contrib import admin
from bookmarks.models import *

class BookmarkAdmin(admin.ModelAdmin):
	list_display = ('title', 'link', 'user')
	list_filter = ('user', )
	ordering = ('title', )
	search_fields = ('title', )

admin.site.register(Link)
admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Tag)
admin.site.register(SharedBookmark)
admin.site.register(Friendship)