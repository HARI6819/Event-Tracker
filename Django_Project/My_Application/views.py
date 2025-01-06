from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Eventdatapaper
from .models import Eventdataproject
from .models import Eventdatatechnical
from django.contrib.auth import logout
from django.contrib import messages


def logout_view(request):
    logout(request)
    return redirect('/loginpage')

def home(request):
    return render(request,"mainpage.html")

def page(request):
    return render(request,"loginpage.html")

def index1(request):
    return render(request,"index1.html")

def sign(request):
    return render(request,"sign.html")

def login(request):
    return render(request,"loginpage.html")

def camera(request,id):
    mydata=Eventdatapaper.objects.get(id=id)
    return render(request,"camera.html",{'datass':mydata})

def cameraproject(request,id):
    mydata=Eventdataproject.objects.get(id=id)
    return render(request,"cameraproject.html",{'datass':mydata})

def cameratechnical(request,id):
    mydata=Eventdatatechnical.objects.get(id=id)
    return render(request,"cameratechnical.html",{'datass':mydata})


# Paper Part

def index(request):
    if(request.method=="POST"):
        name = request.POST['name']
        roll = request.POST['roll']
        email = request.POST['email']
        event_name = request.POST['e_name']
        event_cordinator = request.POST['e_cordinator']
        event_date = request.POST['e_date']
        
        obj=Eventdatapaper()
        obj.Name = name
        obj.Roll_no = roll
        obj.Email = email
        obj.Event_name = event_name
        obj.Event_cordinator = event_cordinator
        obj.Event_date = event_date
        obj.save()
        
    
        mydata=Eventdatapaper.objects.all()
        mydatapro=Eventdataproject.objects.all()
        mydatatech=Eventdatatechnical.objects.all()
        return render(request, "mainpage.html", {'datas': mydata, 'datasproject': mydatapro, 'datastechnical': mydatatech})
    mydata=Eventdatapaper.objects.all()
    mydatapro=Eventdataproject.objects.all()
    mydatatech=Eventdatatechnical.objects.all()
    return render(request,"mainpage.html",{'datas':mydata,'datasproject':mydatapro,'datastechnical':mydatatech})


def update(request,id):
    mydata=Eventdatapaper.objects.get(id=id)
    if (request.method=="POST"):
        name = request.POST['name']
        roll = request.POST['roll']
        email = request.POST['email']
        event_name = request.POST['e_name']
        event_cordinator = request.POST['e_cordinator']
        event_date = request.POST['e_date']

        mydata.Name = name
        mydata.Roll_no = roll
        mydata.Email = email
        mydata.Event_name = event_name
        mydata.Event_cordinator = event_cordinator
        mydata.Event_date = event_date
        mydata.save()


        return redirect('paper1')

    return render(request,"mainpage.html",{'data':mydata})


def upload(request,id):
    mydata=Eventdatapaper.objects.get(id=id)
    if (request.method == 'POST'):
        lati = request.POST['latitude']
        longi = request.POST['longitude']
        lt = request.POST['locationtime']
        ld = request.POST['locationdate']
        place = request.POST['place']
        dis = request.POST['District']

        mydata.Latitude = lati
        mydata.Longitude = longi
        mydata.Time = lt
        mydata.Date = ld
        mydata.Place = place
        mydata.District = dis
        mydata.save()

        if len(request.FILES) !=0:
            mydata.Image = request.FILES['photo']
        mydata.save()
        messages.success(request, "successfully")
        return redirect('paper1')
    return render(request,"mainpage.html",{'data':mydata })

def delete(request,id):
    mydata=Eventdatapaper.objects.get(id=id)
    mydata.delete()
    return redirect('paper1')

# Project Part

def project(request):
    if(request.method=="POST"):
        name = request.POST['name']
        roll = request.POST['roll']
        email = request.POST['email']
        event_name = request.POST['e_name']
        event_cordinator = request.POST['e_cordinator']
        event_date = request.POST['e_date']

        obj=Eventdataproject()
        obj.Name = name
        obj.Roll_no = roll
        obj.Email = email
        obj.Event_name = event_name
        obj.Event_cordinator = event_cordinator
        obj.Event_date = event_date
        obj.save()

        mydata=Eventdataproject.objects.all()
        return render(request,"mainpage.html",{'datasproject':mydata})
    mydata1=Eventdataproject.objects.all()
    return render(request,"mainpage.html",{'datasproject':mydata1})


def updateproject(request,id):
    mydata=Eventdataproject.objects.get(id=id)
    if (request.method=="POST"):
        name = request.POST['name']
        roll = request.POST['roll']
        email = request.POST['email']
        event_name = request.POST['e_name']
        event_cordinator = request.POST['e_cordinator']
        event_date = request.POST['e_date']

        mydata.Name = name
        mydata.Roll_no = roll
        mydata.Email = email
        mydata.Event_name = event_name
        mydata.Event_cordinator = event_cordinator
        mydata.Event_date = event_date
        mydata.save()

        return redirect('project1')

    return render(request,"mainpage.html",{'data':mydata})


def uploadproject(request,id):
    mydata=Eventdataproject.objects.get(id=id)
    if (request.method == 'POST'):
        lati = request.POST['latitude']
        longi = request.POST['longitude']
        lt = request.POST['locationtime']
        ld = request.POST['locationdate']
        place = request.POST['place']
        dis = request.POST['District']

        mydata.Latitude = lati
        mydata.Longitude = longi
        mydata.Time = lt
        mydata.Date = ld
        mydata.Place = place
        mydata.District = dis
        mydata.save()

        if len(request.FILES) !=0:
            mydata.Image = request.FILES['photo']
        mydata.save()
        messages.success(request, "successfully")
        return redirect('project1')
    return render(request,"mainpage.html",{'data':mydata })




def deleteproject(request,id):
    mydata=Eventdataproject.objects.get(id=id)
    mydata.delete()
    return redirect('project1')




# Technical Part

def technical(request):
    if(request.method=="POST"):
        name = request.POST['name']
        roll = request.POST['roll']
        email = request.POST['email']
        event_name = request.POST['e_name']
        event_cordinator = request.POST['e_cordinator']
        event_date = request.POST['e_date']

        obj=Eventdatatechnical()
        obj.Name = name
        obj.Roll_no = roll
        obj.Email = email
        obj.Event_name = event_name
        obj.Event_cordinator = event_cordinator
        obj.Event_date = event_date
        obj.save()

        mydata=Eventdatatechnical.objects.all()
        return render(request,"mainpage.html",{'datastechnical':mydata})
    mydata1=Eventdatatechnical.objects.all()
    return render(request,"mainpage.html",{'datastechnical':mydata1})


def updatetechnical(request,id):
    mydata=Eventdatatechnical.objects.get(id=id)
    if (request.method=="POST"):
        name = request.POST['name']
        roll = request.POST['roll']
        email = request.POST['email']
        event_name = request.POST['e_name']
        event_cordinator = request.POST['e_cordinator']
        event_date = request.POST['e_date']

        mydata.Name = name
        mydata.Roll_no = roll
        mydata.Email = email
        mydata.Event_name = event_name
        mydata.Event_cordinator = event_cordinator
        mydata.Event_date = event_date
        mydata.save()

        return redirect('technical')

    return render(request,"mainpage.html",{'data':mydata})




def uploadtechnical(request,id):
    mydata=Eventdatatechnical.objects.get(id=id)
    if (request.method == 'POST'):
        lati = request.POST['latitude']
        longi = request.POST['longitude']
        lt = request.POST['locationtime']
        ld = request.POST['locationdate']
        place = request.POST['place']
        dis = request.POST['District']

        mydata.Latitude = lati
        mydata.Longitude = longi
        mydata.Time = lt
        mydata.Date = ld
        mydata.Place = place
        mydata.District = dis
        mydata.save()

        if len(request.FILES) !=0:
            mydata.Image = request.FILES['photo']
        mydata.save()
        messages.success(request, "successfully")
        return redirect('technical')
    return render(request,"mainpage.html",{'data':mydata })


def deletetechnical(request,id):
    mydata=Eventdatatechnical.objects.get(id=id)
    mydata.delete()
    return redirect('technical')



def admin1(request):
    mydata=Eventdatapaper.objects.all()
    mydatapro=Eventdataproject.objects.all()
    mydatatech=Eventdatatechnical.objects.all()
    return render(request,"mainpage.html",{'datas':mydata,'datasproject':mydatapro,'datastechnical':mydatatech})

def adminpaper(request):
    mydata=Eventdatapaper.objects.all()
    mydatapro=Eventdataproject.objects.all()
    mydatatech=Eventdatatechnical.objects.all()
    return render(request,"mainpage.html",{'datas':mydata,'datasproject':mydatapro,'datastechnical':mydatatech})