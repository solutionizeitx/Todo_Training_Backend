

from django.urls import path

from Todoapp.views import Todo_item_view

urlpatterns = [
    path('', Todo_item_view.as_view())
]