from django.contrib import admin
from .models import User, Group, Entry
# Registered models: 
admin.site.register(User)
admin.site.register(Group)
admin.site.register(Entry)