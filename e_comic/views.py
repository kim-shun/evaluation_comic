from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from e_comic.forms import NewUserForm

class IndexView(generic.TemplateView):
  template_name = "index.html"

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

class ComicCreateView(generic.TemplateView):
  template_name = "comic_create.html"
