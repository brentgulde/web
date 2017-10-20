from django.forms import ModelForm
from django import forms
from .models import Student, Section

class StudentForm(ModelForm):
    
    class Meta:
        model = Student
        fields = ['name','age','gender','course','year','section_id']


class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = ['section_name','section_room']