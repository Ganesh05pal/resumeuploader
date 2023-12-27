from django.db import models

# Create your models here.
STATE_CHOICE =(
    ('Andhra Pradesh' , 'Andhra Pradesh'),
    ('Karnataka' , 'Karnataka'),
    ('Gujarat' , 'Gujarat'),
    ('Goa' , 'Goa'),
    ('Uttar Pradesh	' , 'Uttar Pradesh'),
    ('Uttarakhand' , 'Uttarakhand'),
    ('West Bengal	' , 'West Bengal'),
    ('Tripura' , 'Tripura'),
    ('Telangana	' , 'Telangana'),
    ('Tamil Nadu' , 'Tamil Nadu'),
    ('Sikkim' , 'Sikkim'),
    ('Rajasthan' , 'Rajasthan'),
    ('Punjab' , 'Punjab'),
    ('Odisha' , 'Odisha'),
    ('Nagaland' , 'Nagaland'),
    ('Mizoram' , 'Mizoram'),
    ('Meghalaya	' , 'Meghalaya'),
    ('Manipur' , 'Manipur'),
    ('Maharashtra' , 'Maharashtra'),
    ('Madhya Pradesh' , 'Madhya Pradesh	'),
    ('Kerala' , 'Kerala'),
    ('Jharkhand' , 'Jharkhand'),
    ('Himachal Pradesh	','Himachal Pradesh	'),
    ('Haryana','Haryana'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Bihar','Bihar'),
    ('Assam','Assam'),
    ('Arunachal Pradesh	','Arunachal Pradesh'),
)
class Resume(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False , auto_now_add=False)
    gender=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin=models.PositiveIntegerField()
    state=models.CharField(choices=STATE_CHOICE, max_length=150)
    mobile=models.PositiveIntegerField()
    job_city=models.CharField(max_length=50)
    email=models.EmailField()
    profile_image=models.ImageField(upload_to="profileimage",blank=True)
    my_file=models.FileField(upload_to="doc",blank=True)
