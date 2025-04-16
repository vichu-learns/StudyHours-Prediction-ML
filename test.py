# Test URL formatting logic

# Sample YouTube URLs
urls = [
    "https://youtu.be/dQw4w9WgXcQ",
    "https://youtube.com/shorts/dQw4w9WgXcQ",
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
]

for url in urls:
    ytLink = url.strip()

    # Ensure the URL is in the correct format
    if "youtu.be/" in ytLink:
        ytLink = ytLink.replace("youtu.be/", "www.youtube.com/watch?v=")
    elif "youtube.com/shorts/" in ytLink:
        ytLink = ytLink.replace("youtube.com/shorts/", "youtube.com/watch?v=")

    print("Formatted URL:", ytLink)
