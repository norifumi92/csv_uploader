from django import forms  
class ClassroomForm(forms.Form):    
    availablity = forms.FileField() # for creating file input  
    reservation = forms.FileField()