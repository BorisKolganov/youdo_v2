from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from works.views import CreateEmployeeView, UpdateEmployeeView

urlpatterns = [
    url(r'^create_employee/', login_required(CreateEmployeeView.as_view()), name='create_employee'),
    url(r'^update_employee/(?P<pk>\d+)/', login_required(UpdateEmployeeView.as_view()), name='update_employee')
]