from django.shortcuts import render  
from django.http import HttpResponse  
from app.functions import upload_file
#from app.functions import process_csv_file  
from app.forms import ClassroomForm  
from django.template import loader
import csv

def index(request):  
    if request.method == 'POST':  
        classroom = ClassroomForm(request.POST, request.FILES)  
        print(request.FILES)
        if classroom.is_valid():  
            upload_file(request.FILES['availablity'])
            upload_file(request.FILES['reservation'])

            return HttpResponse("File uploaded successfuly")
    else:       
        ###Post ClassroomForm
        classroom = ClassroomForm()  
        return render(request,"index.html",{'form':classroom})  
