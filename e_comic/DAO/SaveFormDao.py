from django.shortcuts import get_object_or_404
from e_comic.models import Comic,ComicEvaluation,EvaluationItem,ComicEvaluationDetail

def getComicEvaluations():
  comic_evaluation_list = ComicEvaluation.objects.all()
  return comic_evaluation_list

def getDateTime():
  latest_time = ComicEvaluation.objects.latest("updated_at")
  latest_time = latest_time.updated_at
  return latest_time

def choiceItem():
  evaluation_items = EvaluationItem.objects.all()
  return evaluation_items

def countChoiceItem():
  item_count = EvaluationItem.objects.all().count()
  return item_count

def saveComic(input_comic_name):
  comic = Comic(comic_name=input_comic_name)
  comic.save()
  
def saveComicEvaluation(input_comic_name,input_score,input_comment):
  saved_comic_name = get_object_or_404(Comic,comic_name=input_comic_name)
  comic_evaluation = ComicEvaluation(comic_score=input_score,comment=input_comment,comic_name=saved_comic_name)
  comic_evaluation.save()

def saveComicEvaluationDetail(input_comic_name,input_item,i):
  saved_comic_name = get_object_or_404(Comic,comic_name=input_comic_name)
  comic_evaluation_pk = get_object_or_404(ComicEvaluation,comic_name=input_comic_name)
  comic_evaluation_detail = ComicEvaluationDetail(evaluation_item_id=i,comic_name=saved_comic_name,parent_fk=comic_evaluation_pk,item_content=input_item)
  comic_evaluation_detail.save()
