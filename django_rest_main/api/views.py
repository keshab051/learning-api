from django.shortcuts import render 
from django.http import JsonResponse
from students.models import student

# Create your views here.
def studentsviews(request):
    students=student.objects.all()
    studentlist=list(students.values())
    print(students)
    return JsonResponse(studentlist, safe=False)