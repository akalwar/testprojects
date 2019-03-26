from rest_framework import serializers
from .models import Employees

class Employeesserializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        #fields = ('firstname', 'lastname')
        fields = '__all__'
