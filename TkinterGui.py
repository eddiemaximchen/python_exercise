import tkinter
import customtkinter
from pytube import YouTube
from PIL import Image, ImageTk
import urllib.request
from io import BytesIO

def startDownload():
    try:
        ytLink=link.get()
        ytObject=YouTube(ytLink)
        video=ytObject.streams.get_highest_resolution()
        video.download()
        title.configure(text=ytObject.title,text_color="black")
        finishLabel.configure(text="")
        finishLabel.configure(text='Downloaded!')
        u = urllib.request.urlopen(ytObject.thumbnail_url)
        raw_data = u.read()
        u.close()
        im = Image.open(BytesIO(raw_data))
        im = im.resize((320,240),Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(im)

        button = tkinter.Button(image=photo,width=320,height=240,compound="c")
        button.image = photo
        button.pack()
    except:
        finishLabel.configure(text="Download Error",text_color="red")


#System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#Adding UI Elements
title=customtkinter.CTkLabel(app,text="Insert a youtube link")
title.pack(padx=10,pady=10)

# link input
url_var=tkinter.StringVar()
link=customtkinter.CTkEntry(app,width=350,height=40,textvariable=url_var)
link.pack()

#finished Downloading
finishLabel=customtkinter.CTkLabel(app,text='')
finishLabel.pack()

#download button
download=customtkinter.CTkButton(app,text="Download",command=startDownload)
download.pack(padx=10,pady=10)
# Run app
app.mainloop() 