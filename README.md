---

## 🎵 YouTube to MP3 Downloader (Using `yt_dlp`)

This script allows you to download high-quality `.mp3` files from YouTube using [`yt_dlp`](https://github.com/yt-dlp/yt-dlp) and `ffmpeg`.

---

### 🛠 Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/yourusername/yt-to-mp3-downloader.git
   cd yt-to-mp3-downloader
   ```

2. **Install required packages:**

   ```bash
   pip install yt-dlp
   ```

3. **Make sure ffmpeg is installed and available in your PATH.**

   * On Windows: You can download from [ffmpeg.org](https://ffmpeg.org/download.html), extract it, and add the `bin/` folder to your system PATH.
   * On Linux/macOS:

     ```bash
     sudo apt install ffmpeg        # Debian/Ubuntu
     brew install ffmpeg            # macOS (Homebrew)
     ```

---

### 🚀 How to Use

Run the script in your terminal:

```bash
python downloader.py
```

Then, paste the YouTube URL when prompted:

```bash
Enter YouTube URL: https://www.youtube.com/watch?v=example
```

The audio will be downloaded and saved as an MP3 file using the video title.

---

### 📂 Output

The downloaded MP3 file will be saved in the current directory with the video’s title as the filename.

---

### ❗ Troubleshooting

* If you see the message `"Except"` during download, it means an error occurred (e.g., bad URL, no ffmpeg).
* Make sure the URL is valid and that `ffmpeg` is properly installed.

---
