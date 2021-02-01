from django.views.generic import RedirectView, TemplateView, CreateView
from django.views.generic.base import TemplateResponseMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect

from django.http import Http404


def my_print(*args, **kwargs):
    raise Http404(*args, **kwargs)


class IndexView(RedirectView, TemplateResponseMixin):
    template_name = 'core/index.html'
    pattern_name = 'get_name'

    def get(self, request):
        if (name := request.GET.get('name')):
            return super().get(request, name=name)
        return self.render_to_response({})


class BeginView(TemplateView):
    template_name = 'core/after_index.html'

    def get_context_data(self, name, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['name'] = name
        return context


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('movie_all')
    template_name = 'registration/register.html'

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.success_url)
        return self.get(request)
