from django.shortcuts import render, redirect
from levelweb.models import Student
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

# def enrol(request):
#       return render(request, 'enrol.html')

def enrol(request):

    if request.method == 'POST':
        
        # # TEXT INPUTS
        # # These inputs must not contain any numerical or special characters
        c_fname = request.POST['c_fname']
        c_lname = request.POST['c_lname']
        school = request.POST['school']
        
        p_fname = request.POST['p_fname']
        p_lname = request.POST['p_lname']

        # # SPECIAL INPUTS
        # # These inputs require a unique pattern of code
        email = request.POST['email']
        phone = request.POST['phone']

        # # MULTI-INPUTS
        # # These inputs were taken from a multi-choice drop down bar
        age = request.POST['age']
        term = request.POST['term']
        heard_from = request.POST['heard_from']
        
        # For Testing purpose only, change () argument
        # print(age)

        # PROBLEM HERE
        # COMMANDS to send these data inputs into database
        student = Student()

        student.c_fname = request.POST.get('c_fname')
        student.c_lname = request.POST.get('c_lname')
        student.school = request.POST.get('school')

        student.p_fname = request.POST.get('p_fname')
        student.p_lname = request.POST.get('p_lname')
        student.email = request.POST.get('email')
        student.phone = request.POST.get('phone')

        student.age = request.POST.get('age') 
        student.term = request.POST.get('term')
        student.heard_from = request.POST.get('heard_from')

        student.save()

        # later on may need to check if child registered with parent already exists
        
        return redirect('/')

    else:
        print("data transfered unsuccessful")
        return render(request, 'enrol.html')