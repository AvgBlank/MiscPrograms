from moviepy.editor import VideoFileClip
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

# Load the mp4 file
file = filedialog.askopenfilename(initialdir = "~",title = "Select file",filetypes = ((
        ('Video', '*.mkv'), 
        ('Video', '*.mp4'), 
        ('All Files', '*.*'))))
print(file)
video = VideoFileClip(file)

# Extract audio from video
save = asksaveasfilename(filetypes=[("Audio - MP3", "*.mp3")], defaultextension=[("Audio - MP3", "*mp3")])
print(save)
video.audio.write_audiofile(save)
