from django.shortcuts import render

def new_fuction(request):
    return render(request, 'movies/actor_detail.html', {})
