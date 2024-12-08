from django.contrib import admin
from .models import Message, Blog, Member, Project, Team

admin.site.register(Message)
admin.site.register(Blog)
admin.site.register(Member)
admin.site.register(Project)
admin.site.register(Team)
