# from django.shortcuts import render 
# from django.http import JsonResponse
from students.models import student
from .serializers import studentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def studentsviews(request):
   if request.method == 'GET':
    #   get all the data from the student table
    students = student.objects.all()
    serializer = studentSerializer(students,many = True)
    return Response(serializer.data)