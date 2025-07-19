from django.shortcuts import render,redirect
from .models import Contact
from .forms import  ContactForm
# Create your views here.

def home(request):
    return render(request,"home.html")

def addcontact(request):
    if request.method=="POST":
        f=ContactForm(request.POST)
        f.save()
        return redirect("/")    
    else:
        f=ContactForm()
        d={'form':f}
        return render(request,'addcontact.html',d)
  
def conlist(request):
    elist=Contact.objects.all
    d={'el':elist}
    return render(request,'contactlist.html',d)

def delete_contact(request,id):
    con=Contact.objects.get(id=id)
    con.delete()
    return redirect('/contactlist')

def edit(request,id):
    con=Contact.objects.get(id=id)
    if request.method=="POST":
        f=ContactForm(request.POST,instance=con)
        f.save()
        return redirect('/contactlist')
    else:
        f=ContactForm(instance=con)
        d={'form':f}
        return render(request,'addcontact.html',d)
    
