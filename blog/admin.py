from django.contrib import admin
from .models import Blog, Comment, Tag, Category

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Category)