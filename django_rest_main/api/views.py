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
from rest_framework import mixins,generics
from blogs.models import Blog,Comment
from blogs.serializers import BlogSerializer , CommentSerializer 
from .paginations import CostumPagination
from Employees.filter import EmployeeFilter
from rest_framework.filters import SearchFilter,OrderingFilter
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
   

   # This is class based api_view 

# class employee(APIView):
#    def get(self , request):
#       employees = employee.objects.all()
#       serializer = EmployeeSerializer(employees , many = True)
#       return Response(serializer.data ,status=status.HTTP_200_OK)
   
#    def post(self , request):
#       serializer = EmployeeSerializer(data = request.data)
#       if serializer.is_valid():
#          serializer.save()
#          return Response(serializer.data , status=status.HTTP_201_CREATED)
#       return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

# class employedetail(APIView):
#    def get_object(self , pk):   
#       try:
#        return employee.objects.get(pk=pk)
#       except employee.DoesNotExist:
#          raise Http404
      
#    def get(self , request , pk):
#       employes =self.get_object(pk)
#       serializer = EmployeeSerializer(employes)
#       return Response(serializer.data , status=status.HTTP_200_OK)
   
#    def put(self , request , pk):
#       employes=self.get_object(pk)
#       serializer = EmployeeSerializer(employes , data = request.data) 
#       if serializer.is_valid():
#          serializer.save()
#          return Response(serializer.data , status = status.HTTP_200_OK)
#       return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
   
#    def delete(self , request , pk):
#       employes = self.get_object(pk)
#       employes.delete()
#       return Response(status = status.HTTP_204_NO_CONTENT)




# This is also class based api_view but using mixins

'''in mixins generic will handel all http status and all other activities like serializing and all will be handeled by mixins


class employees(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
   queryset = employee.objects.all()
   serializer_class = EmployeeSerializer

   def get(self , request):
      return self.list(request)
   def post(self , request):
      return self.create(request)
   

class employedetail( mixins.RetrieveModelMixin , mixins.UpdateModelMixin , mixins.DestroyModelMixin , generics.GenericAPIView ):
   queryset = employee.objects.all()
   serializer_class = EmployeeSerializer

   def get(self,request,pk):
      return self.retrieve(request)
   def put(self,request,pk):
      return self.update(request)
   def delete(self,request,pk):
      return self.destroy(request)

    '''

# employee views section with generics views and custom filter implemented 
class employees(generics.ListAPIView,generics.CreateAPIView):
   queryset = employee.objects.all()
   serializer_class = EmployeeSerializer
   # filterset_fields =['designation'] this is only used for global filtering
   filterset_class = EmployeeFilter
   


class employedetail(generics.RetrieveAPIView , generics.UpdateAPIView , generics.DestroyAPIView):
   queryset = employee.objects.all()
   serializer_class = EmployeeSerializer
   lookup_field = 'pk'


#blogs views section to show nested serialization
# also pagination custom pagination is in this views
# And search filter is implemented
class BlogViews(generics.ListCreateAPIView):
   queryset = Blog.objects.all()
   serializer_class = BlogSerializer
   pagination_class = CostumPagination
   filter_backends = [SearchFilter,OrderingFilter] #'OrderingFilter' will used to order in ascending or des...
   search_fields = ['Blog_title','Blog_body']
   ordering_fields = ['id','Blog_title']
#using caret '^' symbol at the starting of search field will only
#check if there is the given word at the starting of that field
#this 'SearchFilter' module will handle the case sensitiveness of the character
#eg: search_fields = ['^Blog_title']


class CommentViews(generics.ListCreateAPIView):
   queryset = Comment.objects.all()
   serializer_class = CommentSerializer


class Commentdetailview(generics.RetrieveUpdateDestroyAPIView):
   queryset = Comment.objects.all()
   serializer_class = CommentSerializer
   lookup_field = 'pk'


class Blogdetailview(generics.RetrieveUpdateDestroyAPIView):
   queryset = Blog.objects.all()
   serializer_class = BlogSerializer
   lookup_field = 'pk'
