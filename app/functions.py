def upload_file(f):  
    with open('app/static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)

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