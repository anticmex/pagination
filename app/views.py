import urllib
import csv
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):

    return redirect(reverse(bus_stations))



def bus_stations(request):
    current_page = 1
    bus_row = []
    with open('data-398-2018-08-30.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bus_row.append(row)
        paginator = Paginator(bus_row, 10)
        page_number = int(request.GET.get('page', 1))
        page_obj = paginator.get_page(page_number)
        data = page_obj.object_list
        if page_obj.has_next():
            np = page_obj.next_page_number()
            params = request.META.get('PATH_INFO', None) + "?" + urllib.parse.urlencode({'page': np})

        next_page_url = params
        return render(request, 'index.html', context={

            'bus_stations': data,
            'current_page': current_page,
            'prev_page_url': None,
            'next_page_url': next_page_url,
        })


