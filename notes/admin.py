from django.contrib import admin

from . import models
# This code allows the Notes model to be viewable in Django admin portal
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'no_of_likes', 'is_public')

admin.site.register(models.Notes, NotesAdmin)