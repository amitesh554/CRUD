from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from .models import Details



def home(request): 
    
    # There are two method to create objects ----1)Objectname=ModelName(attribute1=value1,attribute2=value2,....)
    #Here we have use .save() method to store Objectname.save()
    
    '''2)  Objectname=ModelName.obejcts.create(
        
        attribute1=value1,...)'''
        
    object=Details(name="Amitesh Rai",address='Gola',phone=6389017179)
    object2=Details.objects.create(
        name="Sit",
        address="Lucknow",
        phone="99393933"
    )
    
    object.save()
    # object2.save()
    
    return render(request,'index.html')

def fetch(request):
    context=Details.objects.filter(Q(name='Amitesh Rai') and Q(address='Lucknow'))
    return render(request,'index.html',{"context":context})

def update(request):
    #//////////////////////////////////////////////////V IMP
    
    #Whenever multiple value is returning then in that case we have to use filter Method
    #For a Single value we can use get_object_or_404(ModelName,id) method(for exception free) else we can use get(id) method
    
    context=get_object_or_404(Details,id=id)
    context.name="Hello"
    context.save()
    return render(request,'index.html',{"context":context})

def delete(request):
    id="Amitesh Rai"
    context=Details.objects.filter(name=id)
    context.delete()

