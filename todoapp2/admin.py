from django.contrib import admin

from .models import todomodel, list_completed_todo


class todoadmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_completed', 'created_at')

admin.site.register(todomodel, todoadmin)

class is_completed_admin(admin.ModelAdmin):
    list_display = ('id', 'todo', 'completed_at')

admin.site.register(list_completed_todo, is_completed_admin)