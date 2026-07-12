import yt_dlp
import player

def getAudio(url, vc):
    print("here")
    with yt_dlp.YoutubeDL({"format": "bestaudio/best"}) as ydl:
        info = ydl.extract_info(url, download=False)
        URLstream = info["url"]
        print(URLstream)
        player.streamToSound(URLstream, vc)





