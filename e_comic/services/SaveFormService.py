from multiprocessing import context
from e_comic.DAO.SaveFormDao import choiceItem,saveComic,saveComicEvaluation

def getChoiceItem():
  evaluation_items = choiceItem()
  # item_contents1 = choiceItem(1)
  # item_contents2 = choiceItem(2)
  # item_contents3 = choiceItem(3)
  # item_contents4 = choiceItem(4)
  # item_contents5 = choiceItem(5)
  # item_contents6 = choiceItem(6)
  # item_contents7 = choiceItem(7)
  context = {
    "evaluation_items" : evaluation_items
    # "item_contents1" : item_contents1,
    # "item_contents2" : item_contents2,
    # "item_contents3" : item_contents3,
    # "item_contents4" : item_contents4,
    # "item_contents5" : item_contents5,
    # "item_contents6" : item_contents6,
    # "item_contents7" : item_contents7,
  }
  return context

def saveForm(input_comic_name,input_score,input_comment):
  saveComic(input_comic_name)
  saveComicEvaluation(input_comic_name,input_score,input_comment)
