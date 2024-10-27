import os
import yt_dlp

def download_youtube_video():
    # Ask user for the YouTube video URL
    url = input("Enter the YouTube video URL: ").strip()
    if not url:
        print("No URL provided. Exiting...")
        return

    # Ask user for the output folder
    output_path = input("Enter the output folder path (leave blank for current folder): ").strip()
    if not output_path:
        output_path = '.'
    else:
        output_path = output_path.replace('"', '').replace("'", '')

    # Create directory if it doesn't exist
    if not os.path.exists(output_path):
        try:
            os.makedirs(output_path)
        except OSError as e:
            print(f"Error creating directory: {e}")
            return

    try:
        # Set download options for a single, combined video+audio file
        ydl_opts = {
            'format': 'best[ext=mp4]',  # Download best available video with audio as a single file
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'noplaylist': True,  # Ensure only a single video is downloaded
        }

        # Download video using yt-dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print(f"Download complete! Saved at: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_youtube_video()
