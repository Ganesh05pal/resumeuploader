from django.shortcuts import render
from django.http import HttpResponse
from .forms import ResumeForm
from .models import Resume
from django.views import View
# Create your views here.

class HomeView(View):
    def get(self,request):
        fm=ResumeForm()
        user=Resume.objects.all()
        return render(request,'myapp/home.html',{'form':fm,'user':user})
    def post(self,request):
        fm=ResumeForm(request.POST ,request.FILES)
        if fm.is_valid():
            fm.save()
            return HttpResponse("User is successfully registered")
            # return render(request,'myapp/home.html',{'form':fm})
           
        


class CandidateView(View):
    def get(self,request,pk):
        print(pk)
        candidate=Resume.objects.get(pk=pk)
        return render(request,'myapp/candidate.html',{'candidate':candidate})        