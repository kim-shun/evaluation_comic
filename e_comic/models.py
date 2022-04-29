from django.db import models
from django.core.validators import MaxValueValidator

class User(models.Model):
    nickname = models.CharField(verbose_name="ニックネーム",max_length=100,null=False,unique=True)
    email = models.EmailField(verbose_name="メールアドレス",max_length=250,null=True,unique=True)
    age = models.PositiveSmallIntegerField(verbose_name="年齢",default=0)

class Comic(models.Model):
    comic_name = models.CharField(verbose_name="漫画名",max_length=128,null=False,unique=True,primary_key=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

class ComicResult(models.Model):
    comic_name = models.ForeignKey(Comic,verbose_name="漫画名",max_length=128,null=False,on_delete=models.PROTECT)
    comic_score = models.PositiveSmallIntegerField(verbose_name="評点",validators=[MaxValueValidator(100)],null=False)
    comment = models.TextField(verbose_name="コメント",null=True)
    #evaluation_result_id = models.PositiveSmallIntegerField(verbose_name="評価結果ID",null=False,unique=True)
    #nickname = models.ForeignKey(User,to_field="nickname",verbose_name="作成者",max_length=100,null=False,on_delete=models.PROTECT)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

# class EvaluationResult(models.Model):
#     evaluation_result_id = models.ForeignKey(ComicResult,to_field='evaluation_result_id',verbose_name="評価結果ID",related_name="results",null=False,unique=True,on_delete=models.PROTECT)
#     evaluation_result = models.CharField(verbose_name="評価内容",max_length=50,null=False)
#     created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
#     updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

# class EvaluationItem(models.Model):
#     evaluation_item_id = models.PositiveSmallIntegerField(verbose_name="評価項目ID",null=False,primary_key=True,unique=True)
#     item_name = models.CharField(verbose_name="評価項目名",max_length=50,null=False)

# class EvaluationItemValue(models.Model):
#     evaluation_item_id = models.ForeignKey(EvaluationItem,verbose_name="評価項目ID",related_name="items",null=False,on_delete=models.PROTECT)
#     item_content = models.CharField(verbose_name="評価内容名",max_length=50,null=False)

