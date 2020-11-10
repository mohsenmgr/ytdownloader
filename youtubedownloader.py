import pytube
from pytube import Playlist

playlist = input("Enter Youtube Playlist URL ") #default https://www.youtube.com/playlist?list=PLk8VC3ZVHVh_2CcYfzMaaS49zWoVk8L3c
output = input("Enter Folder Path ") #default C:/Users/Mohsen/Downloads/yt-playlist-master

playlist = Playlist(playlist)
print('Number of videos in playlist: %s' % len(playlist.video_urls))
for video_url in playlist.video_urls:
    print(video_url)
    youtube = pytube.YouTube(video_url)
    video = youtube.streams.get_audio_only()
    video.download(output)
    print("finished")
print('done')


