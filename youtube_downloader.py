import os
from pytube import YouTube

def download_youtube_video():
    # Ask user for the YouTube video URL
    url = input("Enter the YouTube video URL: ")
    if not url:
        print("No URL provided. Exiting...")
        return

    # Ask user for the output folder
    output_path = input("Enter the output folder path (leave blank for current folder): ").strip()
    if not output_path:
        output_path = '.'
    else:
        # Remove any surrounding quotes
        output_path = output_path.replace('"', '').replace("'", '')

    # Create directory if it doesn't exist
    if not os.path.exists(output_path):
        try:
            os.makedirs(output_path)
        except OSError as e:
            print(f"Error creating directory: {e}")
            return

    try:
        # Create YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream available
        video_stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()

        # Display video details
        print(f"\nTitle: {yt.title}")
        print(f"Views: {yt.views:,}")
        print("Downloading...\n")

        # Download the video
        video_stream.download(output_path=output_path)

        print(f"Download complete! Saved at: {os.path.join(output_path, yt.title + '.mp4')}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_youtube_video()
