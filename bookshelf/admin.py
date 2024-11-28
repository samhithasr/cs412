from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Bookshelf)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Shelves)
admin.site.register(Friend)
admin.site.register(Comment)
admin.site.register(Review)