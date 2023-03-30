from tkinter import *
from yt_dlp import YoutubeDL

def download_video():
  	# Gets the text from the text box
    # "1.0" means "Get text from line 1 starting at character 0"
    url = textbox.get('1.0', END).splitlines()
    
    # Set the download location to the current directory
    ydl_opts = {
        'output': './media'
    }

    # Download the video with mostly default options
    with YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(url)
    
def download_audio():
    urls = T.get('1.0', END).splitlines()

    # Choose the video format with the best audio
    # and then use ffmpeg to extract it and convert to mp3
    ydl_opts = {
        'ffmpeg_location': './ffmpeg/bin',
        'format': 'm4a/bestaudio/best',
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }

    # Download with the above options to get only audio
    with YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(urls)

def updatelabel(e):
    # Update the text at the bottom to show how many links have been added
    # by checking the number of lines. Will not be accurate if there are multiple
    # on one line.
    # There is no scroll bar, so this gives an idea of how many there are
    # if there are more links than the box can visibly hold.
    num_urls = len(textbox.get('1.0', END).splitlines())
    bottomtext.config(text="You have entered " + str(num_urls) + " URL(s).")
        
if __name__ == "__main__":
    # TKinter setup
    root = Tk()
    root.geometry("500x200")
    root.title(" YouTube Video Download ")
    root.configure(bg='#22252b')
    p1 = PhotoImage(file = 'icon.png')
    root.iconphoto(False, p1)

    # Create the text box for entering video urls
    # Works with multiple urls to start multiple downloads at once
    textbox = Text(root, bg='#2d3138', fg='#ccd5e6', height=5, width=100, borderwidth = 0, highlightthickness = 0)

    # When a key is pressed while the label is focused, update it
    textbox.bind("<Key>", updatelabel)
    
    # Set the background color
    # The frame is also used for layout
    f = Frame(root, bg='#22252b')
    
    # Create buttons to start the download process
    b1 = Button(f, text="Download Video", bg='#2d3138', fg='#ccd5e6', command=download_video, borderwidth = 0, highlightthickness = 0, padx=6, pady=6)
    b2 = Button(f, text="Download Audio", bg='#2d3138', fg='#ccd5e6', command=download_audio, borderwidth = 0, highlightthickness = 0, padx=6, pady=6)
    b1.grid(row=0, column=0, padx=6)
    b2.grid(row=0, column=1, padx=6)

    # Create the bottom label.
    bottomtext = Label(root, text = "You have entered 0 URLs.", bg='#22252b', fg='#ccd5e6')
    T.pack(padx=12, pady=6)
    f.pack(padx=12, pady=6)
    bottomtext.pack(padx=12, pady=6)
    root.mainloop()