import django_filters
from .models import Artist, Work

class ArtistFilter(django_filters.FilterSet):
    # Define the filters you want to use
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Artist
        fields = ['name']

class WorkFilter(django_filters.FilterSet):
    work_type = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Work
        fields = ['work_type']