from django.http import HttpResponseRedirect
from django.shortcuts import render
from e_comic.forms import NewUserForm
from e_comic.forms import NewComicForm
from e_comic.models import Comic


def index(request):
  comic_list = Comic.objects.all()
  context = {
    'comic_list' : comic_list
  }
  return render(request, 'index.html', context)

def users(request):
    form = NewUserForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect('../')
    else:
        print('ERROR FORM INVALID')
    context = {
        'form' :form
    }
    return render(request, 'user.html', context)

def comic_create(request):
    form = NewComicForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect('../')
    else:
        print('ERROR FORM INVALID')
    context = {
        'form' :form
    }
    return render(request, 'comic_create.html', context)

