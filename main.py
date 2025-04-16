import tkinter
import customtkinter
import yt_dlp

#Download function
def StartDownload():
    try:
        ytLink = link.get().strip()
        
        #Format link
        if "youtu.be/" in ytLink:
            ytLink = ytLink.replace("youtu.be/", "www.youtube.com/watch?v=")
        elif "youtube.com/shorts/" in ytLink:
            ytLink = ytLink.replace("youtube.com/shorts/", "youtube.com/watch?v=")

        print("Downloading :", ytLink)
        Finishlabel.configure(text="Downloading...")

        #ytdlp options
        ydl_opts={
            'outtmpl': 'D:/yt_downloader_py/%(title)s.%(ext)s',
            'format' : 'bv*+ba/best'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([ytLink])
        
        Finishlabel.configure(text="Download Complete!", text_color="green")

    except Exception as e:
        Finishlabel.configure(text="Download Error", text_color="red")
  

#system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#app frame
app = customtkinter.CTk();
app.geometry("720x480")
app.title("HeyPy YouTube Downloader")

#add UI Elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube Link")
title.pack(padx = 15, pady = 15)

#Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width = 350, height = 40, textvariable = url_var)
link.pack(padx = 10, pady = 10)

#Finish Label
Finishlabel = customtkinter.CTkLabel(app, text="")
Finishlabel.pack()

#Download
download = customtkinter.CTkButton(app, text="Download", command=StartDownload)
download.pack(padx = 10, pady = 10)


#Run app
app.mainloop()