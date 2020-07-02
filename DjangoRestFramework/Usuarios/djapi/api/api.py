#Sirve como un views.py cuando se usaba django
#Funciona como el enlace que recive la información, captura la petición y la envía al serializador
#El serializador crea procesa la petición y devuelve la creación para que el api.py pueda responder

from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status

class UserAPI(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        else: 
                return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)