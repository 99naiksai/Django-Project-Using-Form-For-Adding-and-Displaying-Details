
from django.urls import path
from core import views

urlpatterns = [
    path('' , views.form),
    path('student_info' , views.student_info),
    path('search' , views.search),
    path('info' , views.info),
    path('employee' , views.form1),
    path('emp_info' , views.emp_info),
    path('search1' , views.search1),
    path('info1' , views.info1)

]