from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from Todoapp.models import Todo_item
from Todoapp.serializer import Todo_item_serializer

# Create your views here.
class Todo_item_view(ListAPIView):
    serializer_class = Todo_item_serializer
    model_name = Todo_item

    def get_queryset(self):
        qs = self.model_name.objects.all()
        return qs
    
    def post(self, request):
        print("request:", request.data)
        id = request.data.get("id")
        message = ""

        if id:

            Todo_obj = self.model_name.objects.get(id=id)
            serializer_obj = self.serializer_class(Todo_obj, data= request.data)
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
    
   # def put(self, request):
        #return Response('hello world. iam a put request')
    
    def delete(self, request):
        id = request.GET.get('id')
        print("id:", id)
        self.model_name.objects.filter(id=id).delete()

        return Response(
            {
                'message': 'deleted successfully'
            }
        )