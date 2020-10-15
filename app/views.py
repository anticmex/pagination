import urllib
import csv
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):

    return redirect(reverse(bus_stations))



def bus_stations(request):

    bus_row = []
    with open('data-398-2018-08-30.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bus_row.append(row)
        paginator = Paginator(bus_row, 10)
        current_page = int(request.GET.get('page', 1))

        page_obj = paginator.get_page(current_page)
        data = page_obj.object_list
        page_back = None
        if page_obj.has_next():
            np = page_obj.next_page_number()
            page_next = "?" + urllib.parse.urlencode({'page': np})
            if current_page > 1:
                pp = page_obj.previous_page_number()
                page_back = "?" + urllib.parse.urlencode({'page': pp})

        else:
            page_next = None

        next_page_url = page_next
        return render(request, 'index.html', context={

            'bus_stations': data,
            'current_page': current_page,
            'prev_page_url': page_back,
            'next_page_url': next_page_url,
        })
