import django_filters
from .models import employee


class EmployeeFilter(django_filters.FilterSet) :
    designation = django_filters.CharFilter(field_name='designation',lookup_expr='iexact') #This will need exact all word either in uppercase or in lower
    emp_name = django_filters.CharFilter(field_name='emp_name',lookup_expr='icontains') #This will also give you result even if you enter just first name
    # emp_id = django_filters.RangeFilter(field_name='id') If we want to filter using range , use this . This will only range if it is integer
    id_min = django_filters.CharFilter(method='fiter_by_id_range',label='From_EMP_id')
    id_max = django_filters.CharFilter(method='fiter_by_id_range',label='To_EMP_id')


    class Meta:
        model = employee
        fields = ['designation','emp_name','id_min','id_max']

        
    def fiter_by_id_range(self,queryset,name,value):
        if name == 'id_min':
            return queryset.filter(emp_id__gte=value)
        elif name == 'id_max':
            return queryset.filter(emp_id__lte=value)
        return queryset