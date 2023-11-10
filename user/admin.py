from django.contrib import admin
from .models import Project, Tag, Profile, Skill, Message, Comment
# Register your models here.
admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Message)
admin.site.register(Comment)