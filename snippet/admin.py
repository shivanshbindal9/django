from django.contrib import admin
from snippet.models import Snippet,Comment 
# Register your models here.

admin.site.register(Snippet)
admin.site.register(Comment)
