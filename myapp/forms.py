from django import forms
from .models import Resume


GENDER =(
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other'),

)

JOB_CITY_CHOICES =(
    ('Delhi','Delhi'),
    ('Mumbai','Mumbai'),
    ('Banglore','Banglore'),
    ('Bhopal','Bhopal'),
    ('Badodha','Badodha'),
    ('Indore','Indore'),
    ('Pune','Pune'),
    ('Noida','Noida'),
    ('Raipur','Raipur'),
    ('Mohali','Mohali'),
    ('Kerla','Kerla'),
    ('Gujrat','Gujrat'),


)
class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER,widget=forms.RadioSelect)
    job_city =forms.MultipleChoiceField(label='preferred job locations',choices=JOB_CITY_CHOICES,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Resume
        fields =['id','name','dob','gender','city','locality','state',
                  'email','pin','mobile','job_city','profile_image','my_file']
        
        labels ={'name':'Full Name','dob':'Date of Birth','email':'Email ID',
              'mobile':'Mobile No.','pin':'Pin Code','profile_image':'Profile Image','my_file':'Document'}
        
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),

        }