from django.shortcuts import render, HttpResponse
from home.models import Contact,Gallery,LatestNews_TopImage,LatestNews_column,LatestNews_box1,LatestNews_box2,Index_Profile1
# ,Index_Profile2,Index_Profile3,Index_Profile4
from home.models import Admission_details
from django.contrib import messages
import os, datetime
from django.core.files.storage import FileSystemStorage

# Create your views here.
def indent(request):
    result_in = Index_Profile1.objects.all 
    # result_in2 = Index_Profile2.objects.all 
    # result_in3 = Index_Profile3.objects.all 
    # result_in4 = Index_Profile4.objects.all 
    return render(request, 'index.html',{'Index_Profile1':result_in,})
# 'Index_Profile2':result_in2,'Index_Profile3':result_in3,'Index_Profile4':result_in4

    # return HttpResponse("this is homepage")

def infra(request):
    return render(request , 'trail.html')   

def about(request):
    return render(request, 'trail_2.html') 

def services(request):
    return render(request, 'services.html')



 

def contact(request):
    if request.method == "POST":
        name1 = request.POST.get('name1')
        email1 = request.POST.get('email1')
        phone1 = request.POST.get('phone1')
        desc1 = request.POST.get('desc1')
        contact = Contact(name1=name1, email1=email1, phone1=phone1, desc1=desc1, )
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
 



def index(request):
    if request.method == 'POST' and request.FILES['file']:
        name = request.POST.get('name')
        EmailID = request.POST.get('EmailID')
        gender = request.POST.get('gender')
        DoB = request.POST.get('DoB')
        Permanent_Address = request.POST.get('Permanent_Address')
        PinCode = request.POST.get('PinCode')
        Mob_No = request.POST.get('Mob_No')
        Parents_Mob_No = request.POST.get('Parents_Mob_No')
        HSSC_Stream = request.POST.get('HSSC_Stream')
        Total_Marks = request.POST.get('Total_Marks')
        Marks_Obtained = request.POST.get('Marks_Obtained')


        upload_file = request.FILES['file']
        extension = os.path.splitext(upload_file.name)[1]
        rename = datetime.datetime.now().strftime("%Y_%m_%d %H") + extension
        fss = FileSystemStorage()
        filename = fss.save(rename, upload_file)


        upload_file1 = request.FILES['file1']
        extension1 = os.path.splitext(upload_file1.name)[1]
        rename1 = datetime.datetime.now().strftime("%Y_%m_%d %H_%M") + extension1
        fss1 = FileSystemStorage()
        filename1 = fss1.save(rename1, upload_file1)

        
        upload_file2 = request.FILES['file2']
        extension2 = os.path.splitext(upload_file2.name)[1]
        rename2 = datetime.datetime.now().strftime("%Y_%m_%d %H_%M_%S") + extension2
        fss2 = FileSystemStorage()
        filename2 = fss2.save(rename2, upload_file2)


        index = Admission_details(name=name,EmailID=EmailID,gender=gender,DoB=DoB,Permanent_Address=Permanent_Address,
        PinCode=PinCode,Mob_No=Mob_No,Parents_Mob_No=Parents_Mob_No,HSSC_Stream=HSSC_Stream,Total_Marks=Total_Marks,
        Marks_Obtained=Marks_Obtained,file=rename,file1=rename1,file2=rename2)
        index.save()
        upload_file_path = fss.path(filename)
        upload_file1_path = fss1.path(filename1)
        upload_file2_path = fss2.path(filename2)
        messages.success(request, 'Your Form has been SUBMITTED!')
    return render(request, 'admissions.html')


def gal(request):
    resultsdisplay = Gallery.objects.all()
    return render(request,'gallery.html',{'Gallery': resultsdisplay})


def activ(request):
    return render(request,'activities.html')


def latest(request):
    resdis = LatestNews_TopImage.objects.all()
    res1 = LatestNews_column.objects.all()
    box1 = LatestNews_box1.objects.all()
    box2 = LatestNews_box2.objects.all()
    return render(request, 'latestnews.html',{'LatestNews_TopImage': resdis,'LatestNews_column': res1,'LatestNews_box1':box1,"LatestNews_box2":box2})