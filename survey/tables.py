# coding: utf-8
import django_tables2 as tables

from .models import Message


class BootstrapTable(tables.Table):
    class Meta:
        model = Message
        template = 'django_tables2/bootstrap.html'
        attrs = {'class': 'table table-bordered table-striped table-hover'}
        fields = ()


class MessageTable(BootstrapTable):
    relevant_link = tables.TemplateColumn(verbose_name='Relevant Link', orderable=False,
                                          template_name='django_tables2/link_column.html')
    message = tables.Column(accessor='english_message', verbose_name='Messages')

    template = 'django_tables2/bootstrap.html'

    class Meta:
        model = Message
        fields = (
            'msg_number',
            'audience',
            'sector',
            'adapted_by',
            'desired_output',
            'message_type',
            'message',
            'relevant_link',
        )
