from django.shortcuts import get_object_or_404
from e_comic.models import Comic,ComicEvaluation,EvaluationItemContents

def choiceItem(input_evaluation_item_id):
  evaluation_item = EvaluationItemContents.objects.filter(evaluation_item_id=input_evaluation_item_id).all()
  return evaluation_item

def saveComic(input_comic_name):
  comic = Comic(comic_name=input_comic_name)
  comic.save()
  
def saveComicEvaluation(input_comic_name,input_score,input_comment):
  saved_comic_name = get_object_or_404(Comic,comic_name=input_comic_name)
  comic_evaluation = ComicEvaluation(comic_score=input_score,comment=input_comment,comic_name=saved_comic_name)
  comic_evaluation.save()
