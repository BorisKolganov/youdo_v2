from django.contrib.auth import logout, login
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, RedirectView
from django.views.generic.edit import FormView

from core.forms import RegistrationForm, LoginForm


class IndexView(TemplateView):
    template_name = 'index.html'


class RegistrationView(FormView):
    http_method_names = ['get', 'post']
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        form.save()
        return super(RegistrationView, self).form_valid(form)


class LogoutView(RedirectView):
    url = reverse_lazy('core:index')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class LoginView(FormView):
    http_method_names = ['post', 'get']
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        user = form.cleaned_data.get('user')
        login(self.request, user)
        return super(LoginView, self).form_valid(form)

