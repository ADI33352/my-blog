from django.contrib import admin
from website.models import Article , Comment, Contact, Blog,Blogform
# Register your models here.

admin.site.register(Blog)
admin.site.register(Article)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Blogform)