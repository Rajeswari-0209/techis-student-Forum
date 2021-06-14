from django.shortcuts import render
from rest_framework import viewsets
from techisstudentapp.serializers import StudentSerializer
from .models import Student

class StudentViewSet(viewsets.ModelViewSet):
    
    queryset = Student.objects.order_by('created_at').reverse().all()[:20]
    serializer_class = StudentSerializer
   
Student.objects.order_by('created_at').reverse().all()[:20]
