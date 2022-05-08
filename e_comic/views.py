from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from e_comic.forms import NewUserForm
from e_comic.forms import NewComicForm,ComicFormset
from e_comic.models import Comic,ComicEvaluation
from e_comic.services.SaveFormService import getChoiceItem,saveForm
from e_comic.DAO.SaveFormDao import countChoiceItem,saveComicEvaluationDetail
import csv

def index(request):
  comic_list = Comic.objects.all()
  comic_evaluation_list = ComicEvaluation.objects.all()
  context = {
    'comic_list' : comic_list,
    'comic_evaluation_list' : comic_evaluation_list,
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
        count = countChoiceItem()
        for i in range(count):
            i += 1
            input_item = request.POST[str(i)]
            saveComicEvaluationDetail(input_comic_name,input_item,i)
        return HttpResponseRedirect('../')
    return render(request,'test.html',choice_items)

def csv_export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;  filename="漫画評価.csv"'

    writer = csv.writer(response)
    for evaluation in ComicEvaluation.objects.all():
        writer.writerow([evaluation.comic_name.comic_name, evaluation.comic_score,evaluation.comment,evaluation.created_at])
    return response