import django_filters
from .models import employee

class EmployeeFilter(django_filters.FilterSet) :
    designation = django_filters.CharFilter(field_name='designation',lookup_expr='iexact') #this will need exact all word either in uppercase or in lower
    emp_name = django_filters.CharFilter(field_name='emp_name',lookup_expr='icontains') #this will also give you result even if you enter just first name

    class Meta:
        model = employee
        fields = ['designation','emp_name']    