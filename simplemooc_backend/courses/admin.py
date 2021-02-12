from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Course


# Remove default django permissions admin
admin.site.unregister(Group)


class CourseAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {"slug": ("name", )}


# Register admin
admin.site.register(Course, CourseAdmin)
