
#在后台管理站点注册Profile模型

from django.contrib import admin
from .models import Profile
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','date_of_birth','photo']

admin.site.register(Profile,ProfileAdmin)
