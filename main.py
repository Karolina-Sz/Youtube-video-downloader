import ssl; ssl._create_default_https_context = ssl._create_stdlib_context
from tkinter import *
from pytube import YouTube

window = Tk()
window.geometry = ('350x200')
window.title("My own Youtube video downloader")

lbl = Label(window, text="Hi! Paste url of the video you'd like to download and press the button.")
lbl.grid(column=0, row=0)
link = StringVar()
txt = Entry(window, width=10, textvariable=link)
txt.grid(column=0, row=1)

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(window, text='DOWNLOADED').grid(column=0, row=2)

button = Button(window, text="Download", command = Downloader)
button.grid(column=0, row=2)

window.mainloop()
