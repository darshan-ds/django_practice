from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'home.html', {'name':'Darshan', 'dob': '22 nov 95'})


def add(request):

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])

    result = val1 + val2

    return render(request, 'result.html', {'result': result})