from django import forms
from e_comic.models import User
from e_comic.models import Comic,ComicEvaluation,EvaluationItemContents


class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'

class NewComicForm(forms.ModelForm):
    class Meta():
        model = Comic
        fields = ('comic_name',)

ComicFormset = forms.inlineformset_factory(
    Comic, ComicEvaluation, fields=('comic_score','comment'),
    extra=1, can_delete=False
)

class EvaluationChoiceForm(forms.Form):
    comic_name = forms.CharField(label='漫画名')
    comic_score = forms.CharField(label='評点')
    comment = forms.CharField(widget=forms.Textarea,label='コメント') 

    evaluation_item1 = forms.ModelChoiceField(EvaluationItemContents.objects.filter(evaluation_item_id=1), label='評価項目1',empty_label='選択してください')
    evaluation_item2 = forms.ModelChoiceField(EvaluationItemContents.objects.filter(evaluation_item_id=2), label='評価項目2',empty_label='選択してください')
    evaluation_item3 = forms.ModelChoiceField(EvaluationItemContents.objects.filter(evaluation_item_id=3), label='評価項目3',empty_label='選択してください')
    evaluation_item4 = forms.ModelChoiceField(EvaluationItemContents.objects.filter(evaluation_item_id=4), label='評価項目4',empty_label='選択してください')
    evaluation_item5 = forms.ModelChoiceField(EvaluationItemContents.objects.filter(evaluation_item_id=5), label='評価項目5',empty_label='選択してください')
    evaluation_item6 = forms.ModelChoiceField(EvaluationItemContents.objects.filter(evaluation_item_id=6), label='評価項目6',empty_label='選択してください')
    evaluation_item7 = forms.ModelChoiceField(EvaluationItemContents.objects.filter(evaluation_item_id=7), label='評価項目7',empty_label='選択してください')
    evaluation_item8 = forms.ModelChoiceField(EvaluationItemContents.objects.filter(evaluation_item_id=8), label='評価項目8',empty_label='選択してください')
    evaluation_item9 = forms.ModelChoiceField(EvaluationItemContents.objects.filter(evaluation_item_id=9), label='評価項目9',empty_label='選択してください')