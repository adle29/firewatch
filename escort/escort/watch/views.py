from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django_socketio import events, broadcast, broadcast_channel
from watch.models import *
import json 

# Create your views here.
def index(request):
    template = 'index.html'
    context = {}
    return render(request, template, context)

def getFirefighters(request):
    firefighters = [ f.display() for f in Firefighter.objects.all()]
    data = json.dumps({"data":{"firefighters":firefighters}})
    return HttpResponse(data)


def getGasReading(Request):
    gasReadings = [ f.display() for f in GasReading.objects.all()[offset:]]
    data = json.dumps({"data":{"gas_readings":gasReadings}})
    return HttpResponse(data) 

def getTempReading(Request):
    tempReadings = [ f.display() for f in Firefighter.objects.all()[offset:]]
    data = json.dumps({"data":{"temp_readings":tempReadings}})
    return HttpResponse(data) 


def saveTempReading(Request): 
    if Request.method == 'POST':
        temp_reading_value = Request.POST.get('temp_reading_value', '')
        sim_ccid = Request.POST.get('sim_ccid', '')

        firefighter = Firefighter.objects.filter(sim_ccid=sim_ccid).first()
        newTempReading = TempReading(firefighter=firefighter, value=temp_reading_value)
        newTempReading.save()  

        return HttpResponse(status=200)

def saveGasReading(Request):
    if Request.method == 'POST':
        gas_reading_value = Request.POST.get('gas_reading_value', '')
        sim_ccid = Request.POST.get('sim_ccid', '')

        firefighter = Firefighter.objects.filter(sim_ccid=sim_ccid).first()
        newGasReading = GasReading(firefighter=firefighter, value=gas_reading_value)
        newGasReading.save()  
        return HttpResponse(status=200)

def saveTempReading(Request, sim_ccid):
    if request.method == 'POST':
        pass 