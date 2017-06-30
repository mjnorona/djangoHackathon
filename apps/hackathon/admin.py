from django.contrib import admin
from .models import User, Prompt, Solution, Collaboration, Like, Following

admin.site.register(User)
admin.site.register(Prompt)
admin.site.register(Solution)
admin.site.register(Collaboration)
admin.site.register(Like)
admin.site.register(Following)
