import django_filters
from .models import News
from django_filters import CharFilter

class NewsFilter(django_filters.FilterSet):
    heading_contains = CharFilter(field_name='heading',
                                lookup_expr='icontains')
    class Meta:
        model = News
        fields = ""
        # exclude = ['firstname', 'lastname', 'phone']
