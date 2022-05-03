import uuid
from django.db import models
from django.core.validators import MaxValueValidator

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nickname = models.CharField(verbose_name="ニックネーム",max_length=100,null=False,unique=True)
    email = models.EmailField(verbose_name="メールアドレス",max_length=250,null=True,unique=True)
    age = models.PositiveSmallIntegerField(verbose_name="年齢",default=0)

class Comic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comic_name = models.CharField(verbose_name="漫画名",max_length=128,null=False,unique=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

class ComicResult(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comic_name = models.ForeignKey(Comic,verbose_name="漫画名",max_length=128,null=False,on_delete=models.PROTECT)
    comic_score = models.PositiveSmallIntegerField(verbose_name="評点",validators=[MaxValueValidator(100)],null=False)
    comment = models.TextField(verbose_name="コメント",null=True)
    #evaluation_result_id = models.PositiveSmallIntegerField(verbose_name="評価結果ID",null=False,unique=True)
    #nickname = models.ForeignKey(User,to_field="nickname",verbose_name="作成者",max_length=100,null=False,on_delete=models.PROTECT)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

# class ComicResultDetail(models.Model):
#     evaluation_result_id = models.ForeignKey(ComicResult,to_field='evaluation_result_id',verbose_name="評価結果ID",related_name="results",null=False,unique=True,on_delete=models.PROTECT)

# class EvaluationResult(models.Model):
#     evaluation_result_id = models.ForeignKey(ComicResult,to_field='evaluation_result_id',verbose_name="評価結果ID",related_name="results",null=False,unique=True,on_delete=models.PROTECT)
#     evaluation_result = models.CharField(verbose_name="評価内容",max_length=50,null=False)
#     created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
#     updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

class EvaluationItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    evaluation_item_name = models.CharField(verbose_name="評価項目名",max_length=50,null=False,unique=True)

class EvaluationItemValue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    evaluation_item_name = models.ForeignKey(EvaluationItem,verbose_name="評価項目名",related_name="items",null=False,on_delete=models.PROTECT)
    item_content = models.CharField(verbose_name="項目内容名",max_length=50,null=False)

