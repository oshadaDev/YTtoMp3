import yt_dlp

def download_mp3(youtube_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',  # Saves as the video title
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
    except:
        print("Except")
    finally:
        print("\nDownload complete")

# Example usage:
url = input("Enter YouTube URL: ")
download_mp3(url)
