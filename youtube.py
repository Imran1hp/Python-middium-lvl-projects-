from yt_dlp import YoutubeDL

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

ydl_opts = {
    # This tells yt-dlp to pick the best video+audio combined stream
    'format': 'bestvideo+bestaudio/best',
    # Automatically merge into MP4 (or MKV if necessary)
    'merge_output_format': 'mp4',
    # Where to save the file
    'outtmpl': 'Downloads/%(title)s.%(ext)s',
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download completed successfully!")
