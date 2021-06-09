from django.views.generic.base import TemplateView
from django_filters.views import FilterView
from django.db.models import F, Q, Sum, Count
from json_tag import dumps
from django_tables2 import MultiTableMixin, RequestConfig, SingleTableView
from django_tables2.export.views import ExportMixin

from .models import Message
from .tables import MessageTable
from .filters import MessageFilter


class MessageList(
    FilterView,
    ExportMixin,
    SingleTableView,
    RequestConfig):
    table_class = MessageTable
    model = Message
    template_name = 'dashboard.html'
    table = MessageTable(Message.objects.all(), order_by='msg_number')

    filterset_class = MessageFilter

    def get_queryset(self):
        return Message.objects.all().order_by('msg_number')
