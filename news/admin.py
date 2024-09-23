from django.contrib import admin
from .models import News, Author


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')  #
    search_fields = ('title', 'author__first_name', 'author__last_name')
    list_filter = ('publication_date', 'author')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'bio')
    search_fields = ('first_name', 'last_name')
