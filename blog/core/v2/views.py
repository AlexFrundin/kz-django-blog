from django.http import JsonResponse


def begin(request, name):
    return JsonResponse({'name': name*3})


def write(request, name):
    return JsonResponse({'name': name, 'version': 'v2'})


class WriteView(TemplateView):
    template_name = 'core/register.html'

    def get_context_data(self, name, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['name'] = name
        return context

    def get(self, request, name):
        return self.render_to_response(self.get_context_data(name))

    def post(self, request, name):
        data = request.POST
        if data['password'] == data['password2'] and name not in data['login']:
            messages.success(request, message='Ура! Наша дружба стала крепче!')
            return redirect('movie_all')
        messages.add_message(request,
                             message='Вы бяка! Я с вами не дружу!!!',
                             level=messages.WARNING)
        return self.get(request, name)
