import vlc
import time

url = 'http://krelez.chris-the-tuner.de:15000/chiptuneradio_lqmp3'

#define VLC instance
instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

#Define VLC player
player=instance.media_player_new()

#Define VLC media
media=instance.media_new(url)

#Set player media
player.set_media(media)

#Play the media
player.play()

banana = 1
while True:
    to_do = input("Press any key to pause/start:")
    if banana == 1:
        banana = 0
        player.pause()
        player.stop
    else:
        banana = 1
        player.play()


