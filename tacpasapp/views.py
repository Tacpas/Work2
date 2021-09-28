from django.shortcuts import render
from tacpasapp import models


# Create your views here.
def index(request):
    if request.method=="POST":
        name =  request.POST['Name']
        email =  request.POST['email']
        message =  request.POST['message']
        # print(name,email,message)
        ins=models.Contact(name=name, email=email, message=message)
        ins.save()
        print("The data has been written into db")
    
    return render (request,'index.html')
