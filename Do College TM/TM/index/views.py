from django.shortcuts import render
from index import forms
import datetime
from index.models import student
# Create your views here.
#new_time = 0 
#finish_time = 0
def Hiroyuki(request):
    student_data = student.objects.filter(name = "Hiroyuki")
    dict = {"record":student_data}
    return render(request,'Hiroyuki.html' , context = dict)
def Shotaro(request):
    student_data = student.objects.filter(name = "Shotaro")
    dict = {"record":student_data}
    return render(request,'Shotaro.html' , context = dict)
def Rui(request):
    student_data = student.objects.filter(name = "Rui")
    dict = {"record":student_data}
    return render(request,'Rui.html' , context = dict)
def Shinnosuke(request):
    student_data = student.objects.filter(name = "Shinnosuke")
    dict = {"record":student_data}
    return render(request,'Shinnosuke.html' , context = dict)
def Hito(request):
    student_data = student.objects.filter(name = "Hito")
    dict = {"record":student_data}
    return render(request,'Hito.html' , context = dict)
def Aina(request):
    student_data = student.objects.filter(name = "Aina")
    dict = {"record":student_data}
    return render(request,'Aina.html' , context = dict)
def Masaya(request):
    student_data = student.objects.filter(name = "Masaya")
    dict = {"record":student_data}
    return render(request,'Masaya.html' , context = dict)
def Kenji(request):
    student_data = student.objects.filter(name = "Kenji")
    dict = {"record":student_data}
    return render(request,'Kenji.html' , context = dict)
def Ryusei(request):
    student_data = student.objects.filter(name = "Ryusei")
    dict = {"record":student_data}
    return render(request,'Ryusei.html' , context = dict)
def Kento(request):
    student_data = student.objects.filter(name = "Kento")
    dict = {"record":student_data}
    return render(request,'Kento.html' , context = dict)
def Hiroshi(request):
    student_data = student.objects.filter(name = "Hiroshi")
    dict = {"record":student_data}
    return render(request,'Hiroshi.html' , context = dict)
def Shizuka(request):
    student_data = student.objects.filter(name = "Shizuka")
    dict = {"record":student_data}
    return render(request,'Shizuka.html' , context = dict)
def Asahi(request):
    student_data = student.objects.filter(name = "Asahi")
    dict = {"record":student_data}
    return render(request,'Asahi.html' , context = dict)








def record(request):
    record = student.objects.order_by()
    dict = {"record":record}
    return render(request,'record.html' , context = dict)

def time_record(request):
    global new_time
    new_time = datetime.datetime.now()
    #student.objects.update(start_time = new_time)
    dict = {"new_time":new_time}
    return render(request,'time.html' , context = dict)
def finish(request):
    global new_time
    finish_time = datetime.datetime.now()
    print(finish_time)
    print(new_time)
    total_time = finish_time - new_time
    print(total_time)
    total_time = str(total_time)
    total_time = total_time[0:7]
    user = student.objects.all().last()
    user.finish_time =  finish_time
    user.time_minute =  total_time
    user.save()
    # student.objects.update(finish_time =  finish_time, time_minute =  total_time)
    dict = {"finish_time":finish_time,"new_time":new_time, "total_time":total_time }
    return render(request,'finish.html' , context = dict)

def start(request):
    global student_details
    student_form = forms.studentForm()
    student_details = {"student_form": student_form}
    if request.method == "POST": 
        student_form = forms.studentForm(request.POST)
        if student_form.is_valid():
            student.objects.create(name = student_form.cleaned_data["name"], course = student_form.cleaned_data["course"], start_time = datetime.datetime.now(), finish_time = datetime.datetime.now(), time_minute = "value")
            return time_record(request)
    student_details = {"student_form": student_form}   
    return render(request,'start.html' , context = student_details)
