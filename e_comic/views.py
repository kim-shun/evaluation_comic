from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from e_comic.forms import NewUserForm
from e_comic.forms import NewComicForm,ComicFormset,EvaluationChoiceForm
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
    context = {'form': form}
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        formset = ComicFormset(request.POST,instance=post) 
        if formset.is_valid():
            post.save()
            formset.save()
            return HttpResponseRedirect('../')
    else:
        context['formset'] = ComicFormset()
        print('ERROR FORM INVALID')
    
    return render(request, 'comic_create.html', context)

def test(request):
    form = EvaluationChoiceForm()
    context =  {'form': form}
    return render(request,'test.html',context)