from django import forms  
class ClassroomForm(forms.Form):    
    availability = forms.FileField() # for creating file input  
    reservation = forms.FileField()