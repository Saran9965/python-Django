from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import datas
# def a(req):
#     msg='<h1>hi bro</h1>'
#     return HttpResponse(msg)
# def b(req):
#     msg='<h1>hiiii</h1>'
#     return HttpResponse(msg)

# def c(req):
#     msg='<h1>hellow bro</h1>'
#     return HttpResponse(msg)

# GET AND POST METHOD
# def index(req):
#     return render(req,'index.html')

# def result(req):
#     name=req.POST["name"]
#     dept=req.POST["dept"]
#     age=req.POST["age"]
#     file=req.POST["file"]
#     return render(req,'result.html',{'name':name,'dept':dept,'age':age,'file':file})

# using static files using images
# def indexx(req):
#     return render(req,'indexx.html')
# static files
# def indexx(req):
#     return render(req,'indexx.html')


def indexx(req):
    mydata=datas.objects.all()
    if(mydata!=''):
         return render(req,'indexx.html',{'datas':mydata})
    else:
         return render(req,'indexx.html')

def addData(req):
    if req.method=='POST':
        name=req.POST['name']
        age=req.POST['age']
        address=req.POST['address']
        email=req.POST['email']

        obj=datas()
        obj.Name=name
        obj.Age=age
        obj.Address=address
        obj.Email=email
        obj.save()
        mydata=datas.objects.all()
        return redirect('HOME')
        # return render(req,'indexx.html',{'datas':mydata})
    return render(req,'indexx.html')

