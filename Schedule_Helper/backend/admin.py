from django.contrib import admin
from .models import Profiles, Schedule, Groups


@admin.register(Profiles)
class Profile_Admin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'group_id', 'notification', 'deep_link')
    list_filter = ("is_admin", "is_moderator")


@admin.register(Schedule)
class Schedule_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'group_id', 'day', 'number', 'type', 'classroom', 'start_time', 'end_time')


@admin.register(Groups)
class Groups_Admin(admin.ModelAdmin):
    list_display = ('gid', 'faculty', 'gnum')
