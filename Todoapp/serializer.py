from rest_framework import serializers

from Todoapp.models import Todo_item

class Todo_item_serializer(serializers.ModelSerializer): 
    class Meta:
        model = Todo_item
        fields = '__all__'