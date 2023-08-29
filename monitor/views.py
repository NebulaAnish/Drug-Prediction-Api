from django.shortcuts import render

# Create your views here.
import numpy as np 
import pandas as pd 
from .apps import *
from rest_framework.views import APIView
from rest_framework.response import Response

class Prediction(APIView):
    def post(self, request):
        # data = request.DeprecationWarning
        age = request.GET.get("age")
        gender = request.GET.get("gender")
        bp = request.GET.get("bp")
        cholesterol = request.GET.get("cholesterol")
        salt = request.GET.get("salt")
        dtree = ApiConfig.model

        # Predict using independent variables
        PredictionMade = dtree.predict([[age, gender, cholesterol, bp, salt]])
        response_dict = {"Predicted drug": PredictionMade}
        print(response_dict)
        return Response(response_dict, status=200)