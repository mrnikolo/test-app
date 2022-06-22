from django.contrib import admin
from .models import Text

# Register your models here.
# admin.site.register(Text)


@admin.register(Text)
class TestAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'update')
    list_filter = ('update',)
    search_fields = ('slug', 'body')
    prepopulated_fields = {'slug': ('body',)}
    raw_id_fields = ('user', )