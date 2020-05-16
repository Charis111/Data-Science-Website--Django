from django.contrib import admin
from .models import Chart,DataProcess,Post,MessageUs
from django.db import models

# Register your models here.


admin.site.register(Chart)
admin.site.register(DataProcess)
admin.site.register(Post)
admin.site.register(MessageUs)
