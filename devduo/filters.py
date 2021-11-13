import django_filters
from .models import Field, Mentor, Technology


class MentorFilter(django_filters.FilterSet):
    technologies = django_filters.ModelMultipleChoiceFilter(
        field_name='technologies',
        to_field_name='id',
        queryset=Technology.objects.all()
    )

    # technologies_in = django_filters.ModelMultipleChoiceFilter(
    #     field_name='technologies',
    #     to_field_name='id',
    #     queryset=Technology.objects.all(),
    #     lookup_expr='in'
    # )

    fields = django_filters.ModelMultipleChoiceFilter(
        field_name='fields',
        to_field_name='id',
        queryset=Field.objects.all()
    )

    min_price = django_filters.NumberFilter(
        field_name="price", lookup_expr='gte')
    manx_price = django_filters.NumberFilter(
        field_name="price", lookup_expr='lte')
    status = django_filters.BooleanFilter(
        field_name='status', lookup_expr='exact'
    )

    class Meta:
        model = Mentor
        fields = ['technologies', 'fields', 'status', 'price']
