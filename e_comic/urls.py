from django.urls import path
from . import views

app_name = "e_comic"
urlpatterns = [
    path('',views.index,name="index"),
    path('users/',views.users,name="users"),
    path('comic-create/',views.comic_create,name="comic_create"),
    path('test/',views.test,name="test"),
    path('export/', views.csv_export, name='csv_export'),
]
