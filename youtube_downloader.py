import os
import yt_dlp
from urllib.parse import urlparse

def sanitize_filename(title):
    """Remove invalid characters from filenames"""
    return "".join(c if c.isalnum() or c in " -_." else "_" for c in title)

def download_video():
    url = input("Enter YouTube video URL: ").strip()
    custom_title = input("Enter title for video: ").strip()
    save_dir = input("Save directory path: ").strip()

    # Sanitize inputs
    safe_title = sanitize_filename(custom_title)
    os.makedirs(save_dir, exist_ok=True)

    ydl_opts = {
        'outtmpl': os.path.join(save_dir, f'{safe_title}.%(ext)s'),
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'merge_output_format': 'mp4',
        'retries': 3,
        'nooverwrites': True,
        'writethumbnail': True,
        'postprocessors': [{
            'key': 'FFmpegMetadata',
        }],
        'progress_hooks': [lambda d: print_progress(d)],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\n✅ Download complete: {os.path.join(save_dir, safe_title)}.mp4")
    except yt_dlp.utils.DownloadError as e:
        print(f"\n❌ Download failed: {str(e).split(';')[0]}")
    except Exception as e:
        print(f"\n⚠️ Unexpected error: {e}")

def print_progress(d):
    if d['status'] == 'downloading':
        progress = d.get('_percent_str', 'N/A')
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        print(f"\r📥 Downloading... {progress} @ {speed} | ETA: {eta}", end='')

if __name__ == "__main__":
    print("YouTube Video Downloader (yt-dlp)")
    download_video()