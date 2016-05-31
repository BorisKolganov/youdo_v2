from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView

from works.models import Employee


class CreateEmployee(CreateView):
    model = Employee
    template_name = 'create_employee.html'
    fields = ['about', 'skills', 'experience']