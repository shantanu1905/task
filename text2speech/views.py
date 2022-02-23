import re
from django.shortcuts import render ,HttpResponse
from django.shortcuts import render , redirect
from django.contrib import messages
from .texttospeech import t2s
import mimetypes
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent



def home(request):
   if request.method == "POST":
      delete()
   return render(request, 'home.html')




#this function ensure to delete all the data created by user 
def delete():
    #code to delete files from media directory
    media_dir = os.path.join(BASE_DIR, 'media')
    for f in os.listdir(media_dir):
        os.remove(os.path.join(media_dir, f))

    #code to delete files from download/processed_video folder
    download_dir = os.path.join(BASE_DIR, 'download')
    for f in os.listdir( download_dir):
        os.remove(os.path.join( download_dir, f))

    





# this function will take input from html form and send input to t2s function , this will process our text to audio file
def text2speech(request):
    if request.method == "POST":
        text= request.POST['textinput']
        voice= request.POST['selectinput']

        print(text , voice)

        t2s(voice , text)

        messages.success(request, 'your text transcrit is successfully converted to mp3 file ')
        return redirect( 'download_page')

    return render(request , "texttoaudio.html")


# this function will directly download processed audio file to client machine
def download_file(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'voice.mp3'
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


# this function is for download page 
def download_page(request):
    return render(request , "download.html")
