from django.urls import path

from .views import (MovieView, MoviesView, MovieCreateView,
                    MovieUpdateView, MovieDelete, ActorView)


urlpatterns = [
    path('all', MoviesView.as_view(), name='movie_all'),
    path('create', MovieCreateView.as_view(), name='movie_create'),
    path('get/<pk>', MovieView.as_view(), name='movie_get'),
    path('update/<pk>', MovieUpdateView.as_view(), name='movie_update'),
    path('delete/<pk>', MovieDelete.as_view(), name='movie_delete'),
    path('actor/<pk>', ActorView.as_view(), name='actor_get'),
    # path('/', ActorsView.as_view(), )
]

# CRUD ~! FULL API
#FULL API -> url + methods = ['GET', 'POST', 'PUT', 'PATH', 'DELETE', 'OPTIONS', 'HEAD', 'PURGE', 'COPY' ]

#movies -> get
#movie + methods
