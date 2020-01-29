from django.shortcuts import render  
from django.http import HttpResponse  
from app.functions import process_files
from app.functions import write_into_csv  
from app.forms import ClassroomForm  
from django.template import loader

def index(request):  
    if request.method == 'POST':  
        classroom = ClassroomForm(request.POST, request.FILES)  
        if classroom.is_valid():  
            availability = request.FILES['availablity']
            reservation = request.FILES['reservation']
            #handle_uploaded_file(request.FILES['file']) 
            #total = process_csv_file(request.FILES['file'])
            #csv_data = [
            #    'Total', total
            #]
            
            #implement process_files
            csv_data = process_files(availability, reservation)

            #download result as a csv format             
            response = write_into_csv(csv_data)
            
            return response
    else:  
        ###Post ClassroomForm
        classroom = ClassroomForm()  
        return render(request,"index.html",{'form':classroom})  
