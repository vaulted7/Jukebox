import discord



def streamToSound(stream, vc):
    print("im here")
    print(vc)
    print(vc.is_connected())
    print(vc.is_playing())
    vc.play(discord.FFmpegPCMAudio(stream, executable="ffmpeg", options="-vn"))
    print("started")