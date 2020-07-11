from django.contrib import admin
from blog.models import Post, BlogComment
# Register your models here.from django_summernote.admin import SummernoteModelAdmin

admin.site.register(BlogComment)


admin.site.register(Post)
