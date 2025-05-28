from django.urls import path 
from . import views
 
urlpatterns = [
  path('students/',views.studentsviews),
  path('student/<int:pk>',views.studentDetail)
]
