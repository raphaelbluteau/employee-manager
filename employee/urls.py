from django.urls import path, re_path
from . import views

urlpatterns = [
    path('employee/', views.EmployeeList.as_view(), name='employee'),
    re_path('employee/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',
            views.EmployeeRetrieveDestroy.as_view(), name='employee_detail'),
]