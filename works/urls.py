from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from works.views import CreateEmployeeView, UpdateEmployeeView, CreateServiceView, ServiceView, MyServicesView, \
    MyEmplServicesView, Order

urlpatterns = [
    url(r'^create_employee/', login_required(CreateEmployeeView.as_view()), name='create_employee'),
    url(r'^update_employee/(?P<pk>\d+)/', login_required(UpdateEmployeeView.as_view()), name='update_employee'),
    url(r'^create/', login_required(CreateServiceView.as_view()), name='create_service'),
    url(r'service_detail/(?P<pk>\d+)/', ServiceView.as_view(), name='service_detail'),
    url(r'^my_services/', MyServicesView.as_view(), name='my_services'),
    url(r'^my_empl_services/', MyEmplServicesView.as_view(), name='my_empl_services'),
    url(r'^create_order', Order.as_view(), name='order')
]