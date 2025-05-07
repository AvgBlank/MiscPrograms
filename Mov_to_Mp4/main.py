from moviepy.editor import VideoFileClip
from tkinter import filedialog
import os


def convert_mov_to_mp4(mov_file_path):
    # Extract the directory and file name without extension
    directory, filename = os.path.split(mov_file_path)
    filename_without_extension = os.path.splitext(filename)[0]

    # Create the output file path with the same name but with .mp4 extension
    output_file_path = os.path.join(directory, filename_without_extension + ".mp4")

    # Load the .MOV video file
    clip = VideoFileClip(mov_file_path)

    # Save the clip as an .MP4 file
    clip.write_videofile(output_file_path, codec="libx264", audio_codec="aac")


# Example usage
if __name__ == "__main__":
    file = filedialog.askopenfilename(
        initialdir="~", title="Select file", filetypes=(("Video", "*.mov"),)
    )
    mov_file_path = file  # Specify the path to your .MOV file
    convert_mov_to_mp4(mov_file_path)
