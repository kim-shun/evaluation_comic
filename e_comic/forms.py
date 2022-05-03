from django import forms
from e_comic.models import User
from e_comic.models import Comic,ComicResult

class NewUserForm(forms.ModelForm): #ModelFormを継承
    class Meta():
        model = User # モデルのインスタンスを生成
        fields = '__all__' # fieldsに__all__をセットすると、モデル内の全てのフィールドをフォームのフィールドに用いる

class NewComicForm(forms.ModelForm):
    class Meta():
        model = Comic
        fields = ('comic_name',)

ComicFormset = forms.inlineformset_factory(
    Comic, ComicResult, fields='__all__',
    extra=1, can_delete=False
)
