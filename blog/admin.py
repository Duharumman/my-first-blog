from django.contrib import admin
from .models import Post, Author, Publish

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Publish)

