from django.contrib import admin
from .models import Wine, Rating, User
admin.site.register(Wine)
admin.site.register(Rating)
admin.site.register(User)