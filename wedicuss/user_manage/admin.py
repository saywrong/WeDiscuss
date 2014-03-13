from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
from user_manage.models import User_group,User_info,User_relation

class User_info_Inline(admin.StackedInline):
    model = User_info
    can_delete = False
    verbose_name_plural = "user_info"

class UserAdmin(UserAdmin):
    inlines = (User_info_Inline,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(User_group)
admin.site.register(User_relation)