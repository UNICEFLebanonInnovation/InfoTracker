from django.utils.translation import ugettext as _

from django_filters import (
    FilterSet,
    ModelChoiceFilter,
    DateRangeFilter,
    DateFromToRangeFilter,
    DateFilter,
    CharFilter,
    ChoiceFilter
)

from .models import Message, Audience, Sector, Type, Output, Source


class MessageFilter(FilterSet):
    audience = ChoiceFilter(choices=Audience.objects.values_list('id', 'name')
                                .order_by('name').distinct(), empty_label='Audience')
    sector = ChoiceFilter(choices=Sector.objects.values_list('id', 'name')
                                .order_by('name').distinct(), empty_label='Sector')
    desired_output = ChoiceFilter(choices=Output.objects.values_list('id', 'name')
                                .order_by('name').distinct(), empty_label='Desired behavior / output')
    message_type = ChoiceFilter(choices=Type.objects.values_list('id', 'name')
                                .order_by('name').distinct(), empty_label='Type of message / driver')

    class Meta:
        model = Message
        fields = {
            'english_message': ['icontains'],
            'audience': ['exact'],
            'sector': ['exact'],
            # 'adapted_by': ['exact'],
            'desired_output': ['exact'],
            'message_type': ['exact'],
        }
