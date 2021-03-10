from time import localtime
from pygame import mixer


h = input('Coloque a hora :   ')
m = input('Coloque o minuto:  ')

while True:
    if localtime().tm_hour == int(h) and localtime().tm_min == int(m):
        print('Acorde!!!!!')
        mixer.init()
        mixer.music.load('music.mp3.mp3')
        mixer.music.play()
        break
