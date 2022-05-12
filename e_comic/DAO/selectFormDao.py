# from asyncio.windows_events import NULL
# from cms.models.mLabelNameModels import MLabelName
from cms.models.mLabelDepsModels import MLabelDeps
from cms.models.mSelectItemModels import MSelectItem

def selectAllLabelDeps():
    lableDepsInfo = MLabelDeps.objects.values()

    return lableDepsInfo


def selectRootLabelDeps():
    lableDepsInfo = MLabelDeps.objects.prefetch_related('label').filter(parent_label_id__isnull=True).order_by('order').all()

    return lableDepsInfo


def selectChildLabelDeps():
    lableDepsInfo = MLabelDeps.objects.select_related('label').filter(parent_label_id__isnull=False).order_by('parent_label_id', 'order').all()

    return lableDepsInfo


def selectSelectList(fcId, itId):
    selectListInfo = MSelectItem.objects.select_related('select').filter(fc_id=fcId, item_id=itId).order_by('order').all()

    return selectListInfo