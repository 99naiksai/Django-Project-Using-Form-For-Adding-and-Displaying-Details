from django.shortcuts import render , HttpResponse
from core.models import Student,Employee

# Create your views here.
def form(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        address=request.POST.get('address')
        city=request.POST.get('city')
        zip=request.POST.get('zip')

        Stud=Student(email=email , password=password , address=address , city=city , zip=zip)
        Stud.save()
        return HttpResponse('datasave')
    return render(request , 'form.html')

def student_info(request):

    stud = Student.objects.all() 
    return render(request , 'stud1.html' , {'stud':stud})

def search(request):
    return render(request , 'search.html')

def info(request):
    query=request.GET.get('search')
    stud=Student.objects.filter(email__contains=query)
    return render(request , 'info.html' , {'stud':stud})



def form1(request):
    if request.method=='POST':
        emp_email=request.POST.get('eemail')
        epassword=request.POST.get('epassword')
        eaddress=request.POST.get('eaddress')
        ecity=request.POST.get('ecity')
        ezip=request.POST.get('ezip')

        Emp=Employee(emp_email=emp_email , epassword=epassword , eaddress=eaddress , ecity=ecity , ezip=ezip)
        Emp.save()
        return HttpResponse('datasave')
    return render(request , 'form1.html')

def emp_info(request):
    emp = Employee.objects.all()
    return render(request , 'emp1.html' , {'emp':emp})

def search1(request):
    return render(request , 'search1.html')

def info1(request):
    q=request.GET.get('search1')
    emp=Employee.objects.filter(emp_email__contains=q)
    return render(request , 'info1.html' , {'emp':emp})






