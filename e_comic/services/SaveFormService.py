from e_comic.DAO.SaveFormDao import choiceItem,saveComic,saveComicEvaluation

def getChoiceItem():
  evaluation_items = choiceItem()
  context = {
    "evaluation_items" : evaluation_items
  }
  return context

def saveForm(input_comic_name,input_score,input_comment):
  saveComic(input_comic_name)
  saveComicEvaluation(input_comic_name,input_score,input_comment)
