from pytubefix import YouTube

url = input("Enter YouTube URL: ")
yt = YouTube(url)

print(f"Downloading: {yt.title}")
# Get the highest resolution
stream = yt.streams.get_highest_resolution()
stream.download(output_path="Downloads")
print("Download Complete!")
