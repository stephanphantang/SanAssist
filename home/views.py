from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import context, loader

from .forms import Cityform
from .pythoncontrol import LaunchAlgo

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Cityform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            return HttpResponseRedirect('/home/show_result')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Cityform()

    return render(request, 'home/index.html', {'form': form})

def show_result(request):
    result = request.POST
    city_name = result['city_name']
    final_list = LaunchAlgo(city_name)
    
    dict_air = final_list[1]
    dict_water = final_list[2]
    reco_oms = final_list[3]

    context = {
            # Total Score
            'total_score': int(final_list[0]),

            # Air Data
            'dict_air_co': int(dict_air['CO']),
            'dict_air_no2': int(dict_air['NO2']),
            'dict_air_PPM10': int(dict_air['PPM10']),
            'PPM2': int(dict_air['PPM2.5']),

            # Water data 
            'dict_water_nitrate': int(dict_water['Nitrate']),
            'dict_water_nitrite': int(dict_water['Nitrite']),

            # Reco OMS Air
            'reco_oms_air_co': reco_oms['Monoxyde de Carbone'],
            'reco_oms_air_no2': reco_oms["Dioxyde d'Azote"],
            'reco_oms_air_PPM10': reco_oms['PM10'],
            'reco_oms_air_PM2': reco_oms['PM2,5'],

            # Reco OMS Water
            'reco_oms_water_nitrate': reco_oms['Nitrate'],
            'reco_oms_water_nitrite': reco_oms['Nitrite'],
            
            }


    return render(request, 'home/show_result.html', context)
