from django import forms
from e_comic.models import User
class NewUserForm(forms.ModelForm): #ModelFormを継承
    class Meta():
        model = User # モデルのインスタンスを生成
        fields = '__all__' # fieldsに__all__をセットすると、モデル内の全てのフィールドをフォームのフィールドに用いる