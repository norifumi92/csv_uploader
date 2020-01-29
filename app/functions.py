import csv
from django.http import HttpResponse  

### Upload files under app/static/upload
def upload_file(f):  
    with open('app/static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)

### Process csv file
def process_csv_file(f):  
    file_data = f.read().decode("utf-8")
    lines = file_data.split("\r\n")
    
    #fetch and add the last value 
    total = 0
    for line in lines:	
        fields = line.split(",")
        value = int(fields[2])
        total += value
    
    return total

### Process csv files
def process_files(availability, reservation):  
    
        """ Description
        :type availability:
        :param availability:
    
        :type reservation:
        :param reservation:
    
        :raises:
    
        :rtype:
        """
        availability_dict = convert_to_dict(availability)
        reservation_dict = convert_to_dict(reservation)
    
        csv_data = []

        courses = list(availability_dict)
    
        for course in courses:
            remaining = availability_dict[course] - reservation_dict[course]
            row = [course, remaining]
            csv_data.append(row)
        return csv_data

def convert_to_dict(file):
    
        """ Description
        :type file:
        :param file:
    
        :raises:
    
        :rtype:
        """
        data = file.read().decode("utf-8-sig")
        lines = data.split("\r\n")
        dict = {}
        for line in lines:	
            fields = line.split(",")
            course = fields[0]
            capacity = int(fields[1])
            dict[course] = capacity

        return dict


def write_into_csv(csv_data):
        """ Description
        :type csv_data:
        :param csv_data:
    
        :raises:
    
        :rtype:
        """
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="download.csv"'
        writer = csv.writer(response)  

        for row in csv_data:
            writer.writerow(row)

        return response

