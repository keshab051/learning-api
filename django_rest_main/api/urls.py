from django.urls import path 
from . import views
 
urlpatterns = [
  path('students/',views.studentsviews),
  path('students/<int:pk>',views.studentDetail),

  path('employee/',views.employees.as_view()),
  path('employee/<int:pk>',views.employedetail.as_view()),

  path('blogs/', views.BlogViews.as_view()),
  path('comments/', views.CommentViews.as_view()),

  path('comments/<int:pk>',views.Commentdetailview.as_view()),
  path('blogs/<int:pk>',views.Blogdetailview.as_view()),
]