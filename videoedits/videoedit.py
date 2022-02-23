#Remove Audio from Video using FFmpeg
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


def filenames(video , audio):
    video_name=video
    audio_name=audio
    return video_name,audio_name

# this function will remove audio from video . which we upload through html form .
def stripaudio(input_file):
    #os.system("ffmpeg") 
    input_path='media/'+ input_file
    output_path='download/videowithoutaudio.mp4'
    os.system("ffmpeg -i " + input_path + " -c copy -an " + output_path) 

# this function will merge audio with video  
def merge(audio):
    video_name='download/videowithoutaudio.mp4' #fixed name
    audio_name='media/'+audio                                    # dynamic audio file name        
    output_path = 'download/mergevideo.mp4'         #fixed output path
    os.system("ffmpeg -i " + video_name + " -i " + audio_name + " -c:v copy -c:a aac " + output_path ) 
    #print("ffmpeg -i " + video_name + " -i " + audio_name + " -c:v copy -c:a aac " + output_path )

  
