from django.contrib import admin

# Register your models here.
from article.models import Article, Comment

class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'pubDateTime']

class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['article', 'content', 'pubDateTime']
    list_display_links = ['article']
    list_filter = ['article', 'content']
    search_fields = ['content']
    list_editable = ['content']

admin.site.register(Article, ArticleModelAdmin)
admin.site.register(Comment, CommentModelAdmin)