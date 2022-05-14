from e_comic.DAO.EComicDao import choiceItem,selectComic,saveComic,saveComicEvaluation

def getDispItem():
  evaluation_items = choiceItem()
  comics = selectComic()
  context = {
    "evaluation_items" : evaluation_items,
    "comics" : comics,
  }
  return context

def saveForm(input_comic_name,input_score,input_comment):
  saveComic(input_comic_name)
  saveComicEvaluation(input_comic_name,input_score,input_comment)
