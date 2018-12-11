from django.contrib import admin
from groups import models
# Register your models here.

class GroupmemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
