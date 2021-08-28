from django.shortcuts import render
from django.views.generic import UpdateView

from .models import Person
from .forms import myUserForm


def index(request):
    message_err = ''
    if request.method == 'POST':
        form = myUserForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            message_err = 'Ошибка!'
    form = myUserForm()
    return render(request, 'index.html', {'form': form, "message_err": message_err})


class id_person_update(UpdateView):
    model = Person
    template_name = 'index.html'
    form_class = myUserForm
