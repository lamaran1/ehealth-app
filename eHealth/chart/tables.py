import django_tables2 as tables
from .models import data_collect

class DataTable(tables.Table):
    class Meta:
        model = data_collect