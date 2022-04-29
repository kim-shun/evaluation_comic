from django.shortcuts import render
from django.views import generic
#from e_comic.models import User
from e_comic.forms import NewUserForm

class IndexView(generic.TemplateView):
  template_name = "index.html"

def users(request): # form登録用のビュー
    form = NewUserForm(request.POST or None) # formのインスタンス作成

    if form.is_valid():
        form.save(commit=True) # form.saveとするとデータが登録される
    else:
        print('ERROR FORM INVALID')
    return render(request, 'user.html', {'form': form})