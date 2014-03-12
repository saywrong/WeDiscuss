from django.contrib import admin

# Register your models here.
from user_manage.models import User_group,User_info,User_relation

admin.site.register(User_group)
admin.site.register(User_info)
admin.site.register(User_relation)