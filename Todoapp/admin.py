from django.contrib import admin

from .models import Todo_item

# Register your models here.
class Todo_item_admin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_completed', 'created_at')

admin.site.register(Todo_item, Todo_item_admin)