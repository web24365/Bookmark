"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# path 어떤 주소로 접속했을 때 어떤 뷰를 동작시킬 것인지
# re_path 어떤 주소(정규표현식)로 접속했을 때 어떤 뷰를 동작시킬 것인지
# 다른 app에 있는 url file을 가져올 수 있다.
from django.urls import path, re_path, include

from bookmark.views import BookmarkListView

urlpatterns = [
    # 1차 url 라우팅에서는 directory 뒤에 slash(/)를 반드시 넣어줘야 한다.
    path('admin/', admin.site.urls),
    path('bookmark/', include('bookmark.urls', namespace='bookmark')),
    path('', BookmarkListView.as_view(), name='index')
]
