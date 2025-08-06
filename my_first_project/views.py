from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from student.models import Student
from .forms import Contact_form

def home(request):
    # Example query using Q objects (OR condition)
    student = Student.objects.filter(Q(first_name='rk') | Q(age__gte=25))

    print(student)  # For debugging; remove in production
    return render(request, 'home.html', {'s': student})

def about(request):
    return render(request, 'about.html')

def contact(request):
    form = Contact_form()
    return render(request, 'contact.html', {'form': form})
