from rest_framework import serializers
from todoapp2.models import todomodel, list_completed_todo

class todoserializer(serializers.ModelSerializer):
    class Meta:
        model = todomodel
        fields = "__all__"

class completed_todo_serializer(serializers.ModelSerializer):
    task_id = serializers.IntegerField(source='todo.id')
    name = serializers.CharField(source='todo.name')

    class Meta:
        model = list_completed_todo
        fields = ['task_id', 'name', 'completed_at']