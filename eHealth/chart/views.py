from django.shortcuts import render
from django.views.generic import ListView
from .models import data_collect
from .tables import DataTable



# Create your views here.


class DataListView(ListView):
    model = data_collect
    template_name = 'tables.html'


def person_list(request):
    table = DataTable(data_collect.objects.all())

    return render (request, "tables.html", {"table": table})