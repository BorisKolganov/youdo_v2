from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView, UpdateView

from works.forms import EmployeeForm
from works.models import Employee


class CreateEmployeeView(CreateView):
    model = Employee
    template_name = 'create_employee.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('core:index')

    def dispatch(self, request, *args, **kwargs):
        try:
            self.request.user.employee
        except Employee.DoesNotExist:
            return super(CreateEmployeeView, self).dispatch(request, *args, **kwargs)

        return HttpResponseRedirect(reverse('core:index'))

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateEmployeeView, self).form_valid(form)


class UpdateEmployeeView(UpdateView):
    model = Employee
    template_name = 'update_employee.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('core:index')

    def dispatch(self, request, *args, **kwargs):
        try:
            if not self.request.user.employee.id == int(kwargs.get('pk')):
                return HttpResponseRedirect(reverse('core:index'))
        except Employee.DoesNotExist:
            return HttpResponseRedirect(reverse('core:index'))
        return super(UpdateEmployeeView, self).dispatch(request, *args, **kwargs)
