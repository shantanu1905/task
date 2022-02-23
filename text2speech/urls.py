from django.contrib import admin
from django.urls import path , include
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('text2speech' ,text2speech, name="text2speech"),
    path('', home, name="home"),
    path('download/', download_file , name="download_file"),
    path('filedwnlwd' ,download_page, name="download_page"),
]
