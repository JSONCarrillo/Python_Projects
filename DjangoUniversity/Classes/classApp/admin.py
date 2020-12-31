from django.contrib import admin

# Register your models here.
from .models import djangoClasses

# registers djangoClasses app
admin.site.register(djangoClasses)
