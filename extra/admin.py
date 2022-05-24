from django.contrib import admin
from extra.models import Categorie, Comment, Publishers


admin.site.register(Categorie)
admin.site.register(Publishers)
admin.site.register(Comment)