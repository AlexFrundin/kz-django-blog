from django.views.generic import (ListView, DetailView, CreateView,
                                  DeleteView, UpdateView, TemplateView)
from django.views.generic.edit import ModelFormMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Movie, Actor
from .forms import MovieForm
from django.http import Http404


def my_print(*args, **kwargs):
    raise Http404(*args, **kwargs)


class BaseModelApi(TemplateView, ModelFormMixin):

    def get_template_names(self):
        prefix = self.request.method
        if prefix in ['PUT', 'PATCH', 'POST']:
            prefix = 'form'
        name = self.model
        return [f'{name}/{name}_{prefix}.html']

    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass

    def patch(self, request):
        pass

    def delete(self, request):
        pass

    def dispatch(self, request):
        pass

    def get_context_data(self):
        pass

    def get_form(self):
        pass

    def get_form_class(self):
        name = f'{self.model}'.title()
        # prefix = f'{self.request.method}'.title()
        self.form_class = eval(f'{name}Form')
        return self.form_class


class MoviesView(ListView):
    model = Movie
    context_object_name = 'movies'


class MovieView(DetailView):
    model = Movie
    context_object_name = 'movie'


class ActorView(DetailView):
    model = Actor
    context_object_name = 'actor'


@method_decorator(login_required, name='dispatch')
class MovieCreateView(CreateView):
    form_class = MovieForm
    template_name = 'movies/movie_form.html'
    success_url = reverse_lazy('movie_all')


@method_decorator(login_required, name='dispatch')
class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_form.html'
    success_url = reverse_lazy('movie_all')


@method_decorator(login_required, name='dispatch')
class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('movie_all')
