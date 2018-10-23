from django.contrib import admin

# Register your models here.
from .models import Profile,NeighbourHood,Post

admin.site.register(Profile)
admin.site.register(NeighbourHood)
admin.site.register(Post)