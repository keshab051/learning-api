# from django.shortcuts import render 
# from django.http import JsonResponse
from students.models import student
from .serializers import studentSerializer,EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from Employees.models import employee
from django.http import Http404
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

@api_view(['GET','PUT','DELETE']) 
def studentDetail(request,pk):
   try:
      students = student.objects.get(pk=pk)
   except student.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   
   if request.method == 'GET':
      Serializer = studentSerializer(students)
      return Response(Serializer.data,status=status.HTTP_200_OK)
   elif request.method == 'PUT':
      serializer = studentSerializer(data = request.data)  #same as post but model serializer sangai model pani diyo vane paticular student janxa jasle garda update garda sajilo hunxa
      if serializer.is_valid():
         serializer.save()
         return Response(serializer,status=status.HTTP_200_OK)
      else:
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   elif request.method == 'delete':
      student.delete
      return Response(status=status.HTTP_204_NO_CONTENT)
   
class employe(APIView):
   def get(self , request):
      employees = employee.objects.all()
      serializer = EmployeeSerializer(employees , many = True)
      return Response(serializer.data ,status=status.HTTP_200_OK)
   
   def post(self , request):
      serializer = EmployeeSerializer(data = request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data , status=status.HTTP_201_CREATED)
      return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

# class employedetail(APIView):
#    def get_object(self , pk):
#       try:
#        return employee.objects.get(pk)
#       except employe.DoesNotExist:
#          raise Http404
#    def get(self , request , pk):
#       employes =self.get_object(pk)
#       serializer = EmployeeSerializer(employedetail.get_object)
#       if serializer.is_valid():
#          serializer.save()
#          return Response(serializer.data , status=status.HTTP_200_OK)
#       return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
#    def post(self , request , pk):
#       return
