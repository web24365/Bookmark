from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
# 항상 모델을 불러와야 한다.
from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    # template_name =
    # bookmark_form.html
    # bookmark_create.html
    template_name_suffix = '_create'
    model = Bookmark
    fields = ['site_name', 'url']
    # 글쓰기(create)가 완료된 후에 이동할 페이지
    # reverse
    # url 패턴 -> url
    # lazy
    # lazy가 없으면 바로 url이 만들어져 있는 형태
    # lazy가 있으면 실행할 때 url을 만들어서 던져줍니다.
    success_url = reverse_lazy('bookmark:index')

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'
    success_url = reverse_lazy('bookmark:index')

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')