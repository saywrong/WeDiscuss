from django.contrib import admin
from wediscuss_main.models import Discuss_group,Discuss_group_joiners,Viewpoints
# Register your models here.

admin.site.register(Discuss_group)
admin.site.register(Discuss_group_joiners)
admin.site.register(Viewpoints)