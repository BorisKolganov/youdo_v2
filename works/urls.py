from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from works.views import CreateEmployee

urlpatterns = [
    url(r'^create_employee/', login_required(CreateEmployee.as_view()), name='create_employee'),
]