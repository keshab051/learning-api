from django.shortcuts import render 
from django.http import JsonResponse

# Create your views here.
def studentsviews(request):
    students={
        'id':'31',
        'name':'keshab',
        'class':'computersince'
    }
    return JsonResponse(students)