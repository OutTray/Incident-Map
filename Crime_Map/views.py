from django.shortcuts import render
from django.http import HttpResponse
import csv

from .models import Incidents

import datetime

# Create your views here.

def index(request):
    now = datetime.datetime.now()

    day = now.strftime("%d")

    if len(day) == 1:
        day = "0" + day

    month = now.strftime("%m")

    if len(month) == 1:
        month = "0" + month

    current_date = now.strftime("%Y") + "." + month + "." + day

    start_date = 0
    end_date = 99999999

    start_date_form = ""
    end_date_form = ""
    
    temp = request.GET.get('start_date')

    if temp is not None and temp != "":
        start_date_form = temp
        start_date = int(temp.replace("-", ""))

    temp = request.GET.get('end_date')

    if temp is not None and temp != "":
        end_date_form = temp
        end_date = int(temp.replace("-", ""))

    obj = Incidents.objects.raw('SELECT * FROM incidents WHERE incident_date <= %s AND incident_date >= %s ORDER BY incident_date DESC, incident_time DESC', [end_date, start_date])
    
    num_results = len(obj)

    button_information = [[0 for c in range(4)] for r in range(len(obj))]

    i = 0

    for x in obj:
        button_information[i][0] = x.id
        button_information[i][1] = x.location
        button_information[i][2] = 0
        button_information[i][3] = []
        i += 1

    i = 0

    for i in range(len(obj)):
        for j in range(len(obj)):
            if button_information[i][1] == button_information[j][1]:
                button_information[i][2] += 1
                button_information[i][3].append(button_information[j][0])

    """
    button_information = {}    

    for x in obj:
        button_information[f'{x.id}'] = [x.location, 0, []]

    for x in obj:
        for y in obj:
            if button_information[f'{x.id}'][0] == button_information[f'{y.id}'][0]:
                button_information[f'{x.id}'][1] += 1
                button_information[f'{x.id}'][2].append(y.id)
    """

    #print(button_information)


    return render(request, "Crime_Map/index.html", {
        "current_date": current_date, 
        "object":obj, 
        "start_date": start_date, 
        "end_date": end_date, 
        "start_date_form": start_date_form,
        "end_date_form": end_date_form,
        "num_results": num_results,
        "button_information": button_information,
        })

def raw_data(request):

    obj = Incidents.objects.all()
    context = {"object":obj}

    return render(request, "Crime_Map/raw_data.html", context)

def data_csv(request):
    response = HttpResponse(
        content_type="text/csv",
        headers={'Content-Disposition': 'attachment; filename="all_data.csv"'}
    )

    obj = Incidents.objects.raw('SELECT * FROM incidents')

    field_names = ['id', 'date_uploaded', 'incident_date', 'incident_time', 'reported_date', 'reported_time', 'location', 'incident_type', 'hyperlinks', 'incident_details', 'suspect_descriptions', 'top_pixels', 'left_pixels']

    writer = csv.writer(response)

    writer.writerow(field_names)

    for row in obj:
        row_values = []
        for field in field_names:
            value = getattr(row, field)
            row_values.append(value)
        writer.writerow(row_values)

    return response

def current_csv(request):

    response = HttpResponse(
        content_type="text/csv",
        headers={'Content-Disposition': 'attachment; filename="current_results.csv"'}
    )

    referer = request.META.get('HTTP_REFERER')

    start_date = 0
    end_date = 99999999

    if referer.find('start_date') != -1 and referer.find('end_date') != -1:
        temp1 = referer.split('?')
        temp2 = temp1[1].split('&')

        temp = temp2[0].split('=')
        if temp[1] != "":
            start_date = int(temp[1].replace("-", ""))

        temp = temp2[1].split('=')
        if temp[1] != "":
            end_date = int(temp[1].replace("-", ""))
        

    obj = Incidents.objects.raw('SELECT * FROM incidents WHERE incident_date <= %s AND incident_date >= %s ORDER BY incident_date DESC, incident_time DESC', [end_date, start_date])


    field_names = ['id', 'date_uploaded', 'incident_date', 'incident_time', 'reported_date', 'reported_time', 'location', 'incident_type', 'hyperlinks', 'incident_details', 'suspect_descriptions', 'top_pixels', 'left_pixels']

    writer = csv.writer(response)

    writer.writerow(field_names)

    for row in obj:
        row_values = []
        for field in field_names:
            value = getattr(row, field)
            row_values.append(value)
        writer.writerow(row_values)

    return response