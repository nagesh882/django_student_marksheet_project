from django.shortcuts import render
from django.http import HttpResponse

def homePage(request):
    # return HttpResponse("Hello Guys!......")
    data={}
    if (request.POST.get("subject1") == "") and (request.POST.get("subject2") == "") and (request.POST.get("subject3") == "") and (request.POST.get("subject4") == "") and (request.POST.get("subject5") == "") and (request.POST.get("subject6") == "") and (request.POST.get("subject7") == "") and (request.POST.get("subject8") == ""):
        return render(request, 'index.html',{"error":True})

    if request.method == "POST":
        a1 = eval(request.POST.get('subject1'))
        a2 = eval(request.POST.get('subject2'))
        a3 = eval(request.POST.get('subject3'))
        a4 = eval(request.POST.get('subject4'))
        a5 = eval(request.POST.get('subject5'))
        a6 = eval(request.POST.get('subject6'))
        a7 = eval(request.POST.get('subject7'))
        a8 = eval(request.POST.get('subject8'))
        t = a1+a2+a3+a4+a5+a6+a7+a8
        per = t*100/800
        if per >=80:
            d = "First Division"
        elif per >=60:
            d = "Second Division"
        elif per >=45:
            d = "Third Division"
        elif per >=35:
            d = "Pass with Grace"
        else:
            d = "Fail"
        data = {
            'total':t,
            "percentage":per,
            "division":d,
        }
    return render(request, 'index.html',data)
