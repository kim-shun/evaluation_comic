import pprint
from random import choices
from secrets import choice

from cms.dao.selectFormDao import selectAllLabelDeps
from cms.dao.selectFormDao import selectRootLabelDeps
from cms.dao.selectFormDao import selectChildLabelDeps
from cms.dao.selectFormDao import selectSelectList
from cms.forms.selectForms import SelectForm

def selectFormService():
    returnList = [] 

    # 動的テーブル行ヘッダ取得
    selectRootLabelInfoList = selectRootLabelDeps()
    selectChildLabelInfoList = selectChildLabelDeps()

    for rootInfo in selectRootLabelInfoList:
        labelDict = getLabelDict(rootInfo, selectChildLabelInfoList)
        returnList.append(labelDict)

    # 動的テーブル選択肢取得
    selectList1 = selectSelectList('CM1','IT1')
    choiceList1  = generateChoiceList(selectList1)

    for info in returnList:
        childList = info['child_label']
        if(len(childList) != 0):
            info['select_forms'] = None
            for child in childList:
                # 項目ID生成
                itId1 = 'IT1-' + child['label_id']
                itId2 = 'IT2-' + child['label_id']
                # 選択肢取得
                selectList2 = selectSelectList('FC1',itId1)
                selectList3 = selectSelectList('FC1',itId2)
                # 選択肢リスト生成
                choiceList2 = generateChoiceList(selectList2)
                choiceList3 = generateChoiceList(selectList3)
                
                sform = SelectForm()                
                sform.fields['select1'].choices = choiceList1
                sform.fields['select2'].choices = choiceList2
                sform.fields['select3'].choices = choiceList3

                child['select_forms'] = sform
        else:
            # 項目ID生成
            itId1 = 'IT1-' + info['label_id']
            itId2 = 'IT2-' + info['label_id']
            # 選択肢取得
            selectList2 = selectSelectList('FC1',itId1)
            selectList3 = selectSelectList('FC1',itId2)
            # 選択肢リスト生成
            choiceList2 = generateChoiceList(selectList2)
            choiceList3 = generateChoiceList(selectList3)

            sform = SelectForm()
            sform.fields['select1'].choices = choiceList1
            sform.fields['select2'].choices = choiceList2
            sform.fields['select3'].choices = choiceList3
            info['select_forms'] = sform

    print(returnList)

    return returnList


def getLabelDict(info, selectChildLabelInfoList):
        labelDict = {}
        childList = []
        labelDict['label_id']=info.label_id
        labelDict['label_name']=info.label.label_name

        childInfoList = selectChildLabelInfoList.filter(parent_label_id=info.label_id).order_by('order')

        for child in childInfoList:
            childLabelDict = getLabelDict(child, selectChildLabelInfoList)
            childList.append(childLabelDict)

        labelDict['child_label'] = childList

        return labelDict


def generateChoiceList(selectList):
    choiceList = []
    for i, slct in enumerate(selectList):
        if i == 0:
            choice = ('', slct.select.select_name)
        else:
            choice = (slct.select_id, slct.select.select_name)

        choiceList.append(choice)
    
    return choiceList
