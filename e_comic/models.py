import uuid
from django.db import models
from django.core.validators import MaxValueValidator

class User(models.Model):
    user_pk = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    nickname = models.CharField(verbose_name="ニックネーム",max_length=100,null=False,unique=True)
    email = models.EmailField(verbose_name="メールアドレス",max_length=250,null=True,unique=True)
    age = models.PositiveSmallIntegerField(verbose_name="年齢",default=0)

class Comic(models.Model):
    comic_pk = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    comic_name = models.CharField(verbose_name="漫画名",max_length=128,null=False,unique=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

class EvaluationItem(models.Model):
    evaluation_item_pk = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    evaluation_item_id = models.PositiveSmallIntegerField(verbose_name="評価項目ID",null=False,unique=True)
    evaluation_item_name = models.CharField(verbose_name="評価項目名",max_length=50,null=False)

class EvaluationItemContents(models.Model):
    evaluation_item_contents_pk = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    parent_fk = models.ForeignKey(EvaluationItem,verbose_name="親キー",db_column="parent_fk",related_name="contents",on_delete=models.PROTECT)
    evaluation_item_id = models.ForeignKey(EvaluationItem,to_field="evaluation_item_id",db_column="evaluation_item_id",verbose_name="評価項目ID",related_name="items",null=False,on_delete=models.PROTECT)
    item_content = models.CharField(verbose_name="項目内容名",max_length=50,null=False)

class ComicEvaluation(models.Model):
    comic_evaluation_pk = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    comic_name = models.ForeignKey(Comic,verbose_name="漫画名",to_field="comic_name",db_column="comic_name",related_name="c_names",max_length=128,null=False,on_delete=models.PROTECT)
    comic_score = models.PositiveSmallIntegerField(verbose_name="評点",validators=[MaxValueValidator(100)],null=False)
    comment = models.TextField(verbose_name="コメント",null=True)
    nickname = models.ForeignKey(User,to_field="nickname",verbose_name="作成者",db_column="created_by",max_length=100,null=True,on_delete=models.PROTECT)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

class ComicEvaluationDetail(models.Model):
    comic_evaluation_detail_pk = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    parent_fk = models.ForeignKey(ComicEvaluation,verbose_name="親キー",db_column="parent_fk",on_delete=models.PROTECT)
    comic_name = models.ForeignKey(Comic,verbose_name="漫画名",to_field="comic_name",db_column="comic_name",related_name="c_names_detail",max_length=128,null=False,on_delete=models.PROTECT)
    evaluation_item_id = models.PositiveSmallIntegerField(verbose_name="評価項目ID",null=False)
    item_content = models.CharField(verbose_name="評価項目内容",max_length=50,null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)