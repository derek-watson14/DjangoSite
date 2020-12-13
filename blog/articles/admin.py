from django.contrib import admin
from .models import Article


def make_published(modeladmin, request, queryset):
    queryset.update(status="p")


make_published.short_description = "Publish selected articles"


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date', 'status')
    search_fields = ['title', 'published']
    ordering = ['date']
    actions = [make_published]

    # Remove add button from a data model
    # def has_add_permission(self, request, obj=None):
    #     return False


admin.site.register(Article, ArticleAdmin)
