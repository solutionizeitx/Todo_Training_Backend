from rest_framework.response import Response
from todoapp2.models import todomodel, list_completed_todo
from rest_framework.generics import ListAPIView
from todoapp2.serializer import todoserializer, completed_todo_serializer


class todoview(ListAPIView):
    serializer_class = todoserializer
    model_name = todomodel

    def get_queryset(self):
        qs = self.model_name.objects.all()
        return qs
    def post(self,request):
        print("request", request.data)
        id = request.data.get("id")
        message = ""
        if id:

            todo_obj = self.model_name.objects.get(id=id)
            serializer_obj = self.serializer_class(todo_obj, request.data)
            message = "Updated successfully"

        else:
            serializer_obj = self.serializer_class(data= request.data)
            message = "Created successfully"

        serializer_obj.is_valid(raise_exception= True)
        serializer_obj.save()

        return Response(
            {
                'message': message,
                'data': serializer_obj.data
            }
        )
    

    def delete(self, request):
        id = request.GET.get('id')
        print("id:", id)
        self.model_name.objects.filter(id=id).delete()

        return Response(
            {
                'message': 'deleted successfully'
            }
        )
    

class list_view(ListAPIView):
    serializer_class = completed_todo_serializer

    def get_queryset(self):
        
        return list_completed_todo.objects.select_related('todo')
    
    def post(self, request, id):


        try:
            task = todomodel.objects.get(id=id)

        

            task.is_completed = True
            task.save()

            list_completed_todo.objects.create(todo=task)

            return Response({"message": "task marked successfully"})
        except todomodel.DoesNotExist:
             return Response({"message": "task not found"}) 


           