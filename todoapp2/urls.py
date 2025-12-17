from django.urls import path
from todoapp2.views import todoview, list_view

urlpatterns = [
    path('', todoview.as_view()),
    path('list/', list_view.as_view()),
    path('list/<int:id>/', list_view.as_view())
]