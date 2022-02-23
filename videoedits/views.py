from django.shortcuts import render ,HttpResponse
from django.shortcuts import render , redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import mimetypes
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

from .videoedit import *


def uploadfile(request):
     if request.method == 'POST' :
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        fileurl = fs.url(filename)
        size=fs.size( filename)

        audiofile = request.FILES['audiofile']
        audiofilename = fs.save(audiofile.name, audiofile)
        audiofileurl = fs.url(filename)
        audiosize=fs.size( audiofilename)
        stripaudio(filename)
        return render(request, 'videoprocessing.html' , {'fileurl': fileurl , 'filename' : filename ,'size':size ,
                                                          'audiofileurl':audiofileurl , 'audiofilenname':audiofilename , 'audiosize':audiosize})
        
     else:
         return render(request, 'videoprocessing.html')



def video_audio_merge(request):
   path=os.path.join(BASE_DIR, 'media')  # insert the path to your directory   
   file_list =os.listdir(path) 
   if request.method == "POST":
      text= request.POST['selectinput']
      print("your file named " + text + " is merging with given audio and video ...........")
      audio_name= request.POST['textinput']
      merge(audio_name)  # we are calling merge function to process our video and audio .
      return redirect( 'video_download_page')

      outfile=os.path.join(BASE_DIR, 'download/final_output/mergevideo.mp4')

      return render(request, 'videomerge.html' , {'outfile': outfile} )


   return render(request, 'videomerge.html',{'files': file_list} )
 


# this function is for download page 
def video_download_page(request):

    return render(request , "viddownload.html" ,)


# this function will directly download processed audio file to client machine
def dwn_file(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'mergevideo.mp4'
    # Define the full file path
    filepath = BASE_DIR + '/download/' + filename
    # Open the file for reading content
    path = open(filepath, 'rb' )
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response
