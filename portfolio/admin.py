from django.contrib import admin
from .models import Project, Blog, About

# Register your models here.
admin.site.register(Project)
admin.site.register(Blog)
admin.site.register(About)