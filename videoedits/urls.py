from django.contrib import admin
from django.urls import path , include
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload', uploadfile, name="uploadfile"),
    path('merge', video_audio_merge , name="mergefile"),
    path('videodownload', dwn_file , name="dwn_file"),
    path('downloadvideo', video_download_page , name="video_download_page"),

    

   
]
