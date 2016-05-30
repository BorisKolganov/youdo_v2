from django.conf.urls import url
from django.contrib.auth.views import logout

from core.views import IndexView, RegistrationView, LogoutView, LoginView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^registration/', RegistrationView.as_view(), name='registration'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^login/', LoginView.as_view(), name='login')
]