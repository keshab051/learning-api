from django.urls import path 
from . import views
 
urlpatterns = [
  path('students/',views.studentsviews),
  path('students/<int:pk>',views.studentDetail),

  path('employee/',views.employees.as_view()),
  path('employee/<int:pk>',views.employedetail.as_view()),
]
