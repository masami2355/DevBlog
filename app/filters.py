import django_filters
from django_filters import DateFilter
from .models import *


class TitleFilter(django_filters.FilterSet):
    #start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    #end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    title = django_filters.CharFilter(lookup_expr='icontains')
    categoly = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Post
        fields = []#'__all__'
        #exclude = ['Post', 'date_created']