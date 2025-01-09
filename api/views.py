from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from firebase_admin import db

class BackEndApi(APIView):
    name = 'Backend API'
    collection_name = 'datos-collections2'

    def get(self, request):
        ref = db.reference(f'{self.collection_name}')
        data = ref.get()
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        ref = db.reference(f'{self.collection_name}')
        current_time = datetime.now()
        custom_format = current_time.strftime("%d/%m/%Y, %I:%M:%S %p").lower().replace('am', 'a. m.').replace('pm', 'p. m.')
        request.data.update({"saved": custom_format})
        new_resource = ref.push(request.data)
        return Response({"id": new_resource.key}, status=status.HTTP_201_CREATED)

class BackendDetailAPI(APIView):
    name =  'Backend API'
    collection_name = 'datos-collections2'

    def get(self, request, pk):
     ref = db.reference(f'{self.collection_name}/{pk}')

     data = ref.get()

     if data is None:
          return Response(
               {"error": "Documento no encontrado"},
               status=status.HTTP_404_NOT_FOUND
          )

     return Response(data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            ref = db.reference(f'{self.collection_name}/{pk}')
            existing_data = ref.get()
            if not existing_data:
                return Response({"error": "Documento no encontrado"}, status=status.HTTP_404_NOT_FOUND)
            if not request.data:
                return Response({"error": "Cuerpo de la solicitud vacío"}, status=status.HTTP_400_BAD_REQUEST)
            ref.update(request.data)
            return Response({"message": "Documento actualizado correctamente"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def delete(self, request, pk):
        try:
            ref = db.reference(f'{self.collection_name}/{pk}')
            existing_data = ref.get()
            if not existing_data:
                return Response({"error": "Documento no encontrado"}, status=status.HTTP_404_NOT_FOUND)
            ref.delete()
            return Response({"message": "Documento eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
