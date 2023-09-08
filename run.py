import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip


root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])

if file_path:
    try:
       
        video_clip = VideoFileClip(file_path)
              
        audio_clip = video_clip.audio
        mp3_file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        if mp3_file_path:
            audio_clip.write_audiofile(mp3_file_path)
            audio_clip.close()
            video_clip.close()
            print(f"Conversion successful. Saved as {mp3_file_path}")
        else:
            print("No output file selected. Conversion canceled.")
    
    except Exception as e:
        print(f"Error: {e}")
else:
    print("No file selected. Conversion canceled.")
