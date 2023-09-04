from django.shortcuts import render

# Create your views here.
from app1.models import *
def insert_school(request):
    if request.method=='POST':
        scn=request.POST['scn']
        scp=request.POST['scp']
        scl=request.POST['scl']
        so=School.objects.get_or_create(scname=scn,scprincipal=scp,sclocation=scl)[0]
        so.save()
        qscl=School.objects.all()
        d={'qscl':qscl}
        return render(request,'display_school.html',d)
    return render(request,'insert_school.html')
def insert_student(request):
    if request.method=='POST':
        scn=request.POST['scn']
        sn=request.POST['sn']
        sid=request.POST['sid']
        so=School.objects.get(scname=scn)
        sto=Student.objects.get_or_create(scname=so,sname=sn,sid=sid)[0]
        sto.save()
        qstl=Student.objects.all()
        d={'qstl':qstl}
        return render(request,'display_student.html',d)
    return render(request,'insert_student.html')