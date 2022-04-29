from django.urls import path
from . import views

app_name = "e_comic"
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('users/',views.users,name="users"),
    path('comic-create/',views.ComicCreateView.as_view(),name="comic_create"),
]
