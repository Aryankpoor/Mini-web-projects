# This program extracts audio from a video file
import moviepy.editor 


# Video path
video = moviepy.editor.VideoFileClip('file.mp4')


#audio conversion
audio = video.audio

audio.write_audiofile('file.mp3')

#Make sure the video file is in same folder as program
#This program requires python installed on computer to run
#But it can also be converted to a simple .exe format
