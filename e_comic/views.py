from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,get_object_or_404
from e_comic.forms import NewUserForm
from e_comic.forms import NewComicForm,ComicFormset
from e_comic.models import Comic,ComicEvaluation
from e_comic.services.SaveFormService import getChoiceItem,saveForm


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
    choice_items = getChoiceItem()
    if request.method == 'POST':
        input_comic_name = request.POST["comic_name"]
        input_score = request.POST["score"]
        input_comment = request.POST["comment"]
        saveForm(input_comic_name,input_score,input_comment)
    return render(request,'test.html',choice_items)