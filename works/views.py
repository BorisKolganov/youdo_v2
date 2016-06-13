from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Count
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView, UpdateView, DetailView, ListView, View

from works.forms import EmployeeForm, ServiceForm
from works.models import Employee, Service


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


class CreateServiceView(CreateView):
    model = Service
    template_name = 'create_service.html'
    form_class = ServiceForm
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateServiceView, self).form_valid(form)


class ServiceView(DetailView):
    model = Service
    template_name = 'service_detail.html'
    context_object_name = 'service'

    def get_context_data(self, **kwargs):
        context = super(ServiceView, self).get_context_data(**kwargs)
        context['employees'] = Employee.objects.filter(servicetype=self.object.type).annotate(service_count=Count('service')).order_by('service_count')[:2]
        context['newbie'] = Employee.objects.filter(servicetype=self.object.type).order_by('?')[0]
        return context


class MyServicesView(ListView):
    model = Service
    template_name = 'my_service_view.html'
    context_object_name = 'services'
    paginate_by = 9

    def get_queryset(self):
        qs = super(MyServicesView, self).get_queryset()
        return qs.filter(user=self.request.user)


class MyEmplServicesView(ListView):
    model = Service
    template_name = 'my_service_view.html'
    context_object_name = 'services'
    paginate_by = 9

    def get_queryset(self):
        qs = super(MyEmplServicesView, self).get_queryset()
        try:
            return qs.filter(employee=self.request.user.employee)
        except Employee.DoesNotExist:
            return []


class Order(View):
    def get(self, request):
        service_id = request.GET.get('service_id')
        employee_id = request.GET.get('employee_id')
        employee = Employee.objects.filter(id=employee_id).first()
        service = Service.objects.filter(id=service_id).first()
        if service.employee:
            return HttpResponseRedirect(request.GET.get('redirect_url'))
        service.employee = employee
        service.save()
        return HttpResponseRedirect(request.GET.get('redirect_url'))
