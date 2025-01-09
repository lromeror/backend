from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from datetime import datetime
	
from firebase_admin import db

class BackEndApi(APIView):
	    
     name = 'Backend API'

     # Coloque el nombre de su colección en el Realtime Database
     collection_name = 'datos-collections'