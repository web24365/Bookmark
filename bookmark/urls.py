from django.contrib import admin
# path 어떤 주소로 접속했을 때 어떤 뷰를 동작시킬 것인지
# re_path 어떤 주소(정규표현식)로 접속했을 때 어떤 뷰를 동작시킬 것인지
from django.urls import path, re_path

from .views import *

app_name = 'bookmark'

urlpatterns = [
    path('', BookmarkListView.as_view(), name='index'),
    path('create/', BookmarkCreateView.as_view(), name='create'),
    # integer, primary key
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
]
