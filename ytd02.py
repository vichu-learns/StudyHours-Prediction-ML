import tkinter
import customtkinter
import yt_dlp
import os

def StartDownload():
    try:
        # Clear any previous status messages
        status_label.configure(text="")
        
        # Get the YouTube link
        ytLink = link.get().strip()
        
        # Validate the link
        if not ytLink:
            raise ValueError("Please enter a YouTube URL")
        
        # Configure yt-dlp options
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': os.path.join(os.path.expanduser("~"), "Downloads", "%(title)s.%(ext)s"),
        }
        
        # Create a yt-dlp object
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract video information
            info_dict = ydl.extract_info(ytLink, download=True)
            
            # Get the downloaded file name
            video_title = info_dict.get('title', None)
            
            # Update status label
            status_label.configure(
                text=f"Download Complete! \nVideo saved to Downloads folder", 
                text_color="green"
            )
        
    except Exception as e:
        # Detailed error handling
        error_message = str(e)
        print(f"Full error: {error_message}")  # Debugging print
        
        # Customize error messages
        if "URL" in error_message:
            error_message = "Invalid YouTube URL. Please check the link."
        elif "unavailable" in error_message.lower():
            error_message = "Video is unavailable or private."
        
        # Update status label with error
        status_label.configure(text=f"Error: {error_message}", text_color="red")

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("HeyPy YouTube Downloader")

# Title
title = customtkinter.CTkLabel(app, text="Insert a YouTube Link", font=("Helvetica", 16))
title.pack(padx=15, pady=15)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var, placeholder_text="Paste YouTube URL here")
link.pack(padx=10, pady=10)

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=StartDownload)
download.pack(padx=10, pady=10)

# Status Label
status_label = customtkinter.CTkLabel(app, text="", font=("Helvetica", 12))
status_label.pack(padx=10, pady=10)

# Run app
app.mainloop()