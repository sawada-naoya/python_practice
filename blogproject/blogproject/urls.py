#ルーティング処理
"""
URL configuration for blogproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

# ブラウザからのリクエスト先のURLがadmin/と一致(https://<ホスト名>/admin)した場合にadmin.site.urlsで定義されているビューを呼び出す。
urlpatterns = [
    path("admin/", admin.site.urls),
    
    # https://ホスト名 へのアクセスはblogappのURLconf(urls.py)を呼び出す
    # include(引数)：指定されたモジュールをインポートするためのパス（名前空間）を取得する
    path('',include('blogapp.urls')),
]
