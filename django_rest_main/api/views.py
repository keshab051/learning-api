# from django.shortcuts import render 
# from django.http import JsonResponse
from students.models import student
from .serializers import studentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def studentsviews(request):
   if request.method == 'GET':
      #   get all the data from the student table
      students = student.objects.all()
      serializer = studentSerializer(students,many = True)
      return Response(serializer.data,status=status.HTTP_200_OK)
   elif request.method == 'POST':
      serializer = studentSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)
      print(serializer)
      return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)        

@api_view(['GET']) 
def studentDetail(request,pk):
   try:
      students = student.objects.get(pk=pk)
   except student.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   
   if request.method == 'GET':
      Serializer = studentSerializer(students)
      return Response(Serializer.data,status=status.HTTP_200_OK)