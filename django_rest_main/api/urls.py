from django.urls import path 
from . import views
 
urlpatterns = [
  path('students/',views.studentsviews),
  path('students/<int:pk>',views.studentDetail)
]
