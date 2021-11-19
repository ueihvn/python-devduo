import django_filters
from .models import Field, Mentor, Technology, Booking, User, Status


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


class BookingFilterClass(django_filters.FilterSet):
    mentor = django_filters.ModelChoiceFilter(
        field_name='mentor',
        to_field_name='id',
        queryset=Mentor.objects.all()
    )

    mentee = django_filters.ModelChoiceFilter(
        field_name='mentee',
        to_field_name='id',
        queryset=User.objects.all()
    )

    status = django_filters.CharFilter(
        field_name='status',
    )

    class Meta:
        model = Booking
        fields = ['mentor', 'mentee', 'status']
