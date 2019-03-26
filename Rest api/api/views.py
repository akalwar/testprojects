from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employees
from .serializers import Employeesserializer

class EmployeeList(APIView):
    def get(self, request):
        emp_obj = Employees.objects.all()
        serializer = Employeesserializer(emp_obj, many= True)
        return Response(serializer.data)

    def post(self):
        pass
