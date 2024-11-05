import os
import pygame
import tkinter
import re
import json

from tkinter import filedialog
from pygame import mixer

pygame.init()
mixer.init()


'''
Main window
'''
screen = pygame.display.set_mode((800,450))
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()
loop = True


'''
Обработка изображений
'''
_image_library = {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

#загрузка всех изображений
play = get_image(r"/Users/ersultanersultan/Desktop/Python/lap7/music/play1.png")
forward = get_image(r"/Users/ersultanersultan/Desktop/Python/lap7/music/forward1.png")
back = get_image(r"/Users/ersultanersultan/Desktop/Python/lap7/music/back1.png")
folder = get_image(r"/Users/ersultanersultan/Desktop/Python/lap7/music/folder.png")
clear = get_image(r"/Users/ersultanersultan/Desktop/Python/lap7/music/clear.png")

#создание прямоугольных объектов для всех изображений
play_rect = play.get_rect(center = (screen.get_rect().center[0], 350))
forward_rect = forward.get_rect(center = (screen.get_rect().center[0]*3/2, 350))
back_rect = back.get_rect(center = (screen.get_rect().center[0]/2, 350))
folder_rect = folder.get_rect(center = (40,40))
clear_rect = clear.get_rect(center = (40,100))


'''
Text Handling
'''

info_rect1 = pygame.Rect(200,50,400,40)
info_rect2 = pygame.Rect(200,150,400,40)
font = pygame.font.Font(None, 36)
def print_text(screen, text, info_rect):
    text_rect = text.get_rect(center = info_rect.center)
    pygame.draw.rect(screen, (40,40,50), info_rect)
    screen.blit(text, text_rect)

'''
Main Class
'''

class MusicPlayer():
    def __init__(self):
        self.channel = mixer.Channel(1)
        self.queue = []
        self.started = False
        self.paused = False
        self.volume = 1.0
        self.index = 0
        self.dynamic_play = get_image(r"/Users/ersultanersultan/Desktop/Python/lap7/music/play1.png")

    def read_songlist(self, path):
        if os.access(path, os.F_OK):
            with open(path, "r") as sl:
                self.queue = json.load(sl)

    def get_songlist(self):
        li = []
        root = tkinter.Tk()
        root.withdraw()
        selection = filedialog.askdirectory(initialdir = "C:", title = "Select a folder")
        for dirpath, dirname, filename in os.walk(selection, "."):
            for f in filename:
                li.append(os.path.join(dirpath,f))

        self.queue.extend(list(filter(re.compile(r".*\.(mp3|ogg|wav|m4a)$").match, li)))

    def save_songlist(self, path):
        with open(path, "w") as sl:
            json.dump(self.queue, sl)

    def play_function(self):
        print(self.queue)
        try:
            self.channel.play(mixer.Sound(self.queue[self.index]))
            self.started = True
            self.dynamic_play= get_image(r"/Users/ersultanersultan/Desktop/Python/lap7/music/pause1.png")
        except:
            print("Nothing to play yet")

    def pause_function(self):
        if self.paused:
            self.paused = False
            self.channel.unpause()
            self.dynamic_play = get_image(r"/Users/ersultanersultan/Desktop/Python/lap7/music/pause1.png")
        else:
            self.paused = True
            self.channel.pause()
            self.dynamic_play = get_image(r"/Users/ersultanersultan/Desktop/Python/lap7/music/pause1.png")

    def stop_function(self):
            self.dynamic_play = get_image(r"/Users/ersultanersultan/Desktop/Python/lap7/music/pause1.png")
            self.started = False
            self.channel.stop()
            self.index = 0

    def back_function(self, prev):
        if prev:
            self.index -= 1
        if self.started and self.index >= 0:
            self.dynamic_play = get_image(r"/Users/ersultanersultan/Desktop/Python/lap7/music/pause1.png")
            self.channel.play(mixer.Sound(self.queue[self.index]))
        else:
            self.stop_function()

    def forward_function(self):
        if self.started:
            print(f"Current index: {self.index}, Queue length: {len(self.queue)}")
            if self.index < len(self.queue) - 1:
                self.index += 1
                try:
                    self.channel.play(mixer.Sound(self.queue[self.index]))
                except Exception as e:
                    print(f"Error playing song: {e}")
                    self.stop_function()
            else:
                self.stop_function()



    def clear_function(self, shift):
        self.stop_function()
        if shift:
            self.queue = []
            os.remove("/Users/ersultanersultan/Desktop/Python/lap7/music/song.json")
        else:
            with open("/Users/ersultanersultan/Desktop/Python/lap7/music/song.json", "r") as sl:
                self.queue = json.load(sl)

    def volume_up(self):
        self.volume += 0.07
        if self.volume <= 1.0:
            self.channel.set_volume(self.volume)
        else:
            self.volume = self.channel.get_volume()

    def volume_down(self):
        self.volume -= 0.07
        if self.volume >= 0:
            self.channel.set_volume(self.volume)
        else:
            self.volume = self.channel.get_volume()


'''
Instantiation of the MusicPlayer Class
'''
music_player = MusicPlayer()
music_player.read_songlist("/Users/ersultanersultan/Desktop/Python/lap7/music/song.json")


'''
The Main Loop
'''
while loop:

    pressed = pygame.key.get_pressed()

    #частые клавиши
    alt = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
    ctrl = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
    shift = pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

        #функции клавиатуры
        if event.type == pygame.KEYDOWN:
            #quitting
            if event.key == pygame.K_w and ctrl:
                loop = False
            if event.key == pygame.K_F4 and alt:
                loop = False
            if event.key == pygame.K_ESCAPE:
                loop = False
            #увеличение и уменьшение громкости
            if event.key == pygame.K_UP:
                music_player.volume_up()
            if event.key == pygame.K_DOWN:
                music_player.volume_down()
            #выбор файла
            if event.key == pygame.K_o and ctrl:
                music_player.get_songlist()
            #воспроизведение и пауза
            if event.key == pygame.K_SPACE and not music_player.started:
                music_player.play_function()
            elif event.key == pygame.K_SPACE and music_player.started:
                music_player.pause_function()
            #назад и вперед
            elif event.key == pygame.K_LEFT:
                music_player.back_function(shift)
            elif event.key == pygame.K_RIGHT:
                music_player.forward_function()
            #очистить очередь и полностью удалить ее
            elif event.key == pygame.K_DELETE:
                music_player.clear_function(shift)
            
        #функция мыши
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #положение мыши
            pos = pygame.mouse.get_pos()
            current_time = pygame.time.get_ticks()

            #выбор файла
            if folder_button.collidepoint(pos):
                music_player.get_songlist()
            #воспроизведение и пауза
            if play_button.collidepoint(pos) and not music_player.started:
                music_player.play_function()
            elif play_button.collidepoint(pos) and music_player.started:
                music_player.pause_function()
            #назад
            elif back_button.collidepoint(pos):
                music_player.back_function(prev=True)
            #вперед
            elif forward_button.collidepoint(pos):
                music_player.forward_function()
            #очистить очередь или удалить ее
            elif clear_button.collidepoint(pos):
                music_player.clear_function(shift)

            last_click_time = current_time

        if not music_player.channel.get_busy() and music_player.started:
            music_player.forward_function()

 
    screen.fill((50,50,60))

    #button images
    play_button = screen.blit(music_player.dynamic_play, play_rect)
    forward_button = screen.blit(forward, forward_rect)
    back_button = screen.blit(back, back_rect)
    folder_button = screen.blit(folder, folder_rect)
    clear_button = screen.blit(clear, clear_rect)

    #если началось воспроизведение, отображается название текущей песни
    if music_player.started:
        text1 = font.render("Now Playing:", True, (255,255,255))
        text2 = font.render(os.path.basename(music_player.queue[music_player.index]), True, (255,255,255))
        print_text(screen, text1, info_rect1)
        print_text(screen, text2, info_rect2)

    pygame.display.flip()
    clock.tick(90)

#после закрытия последняя версия очереди записывается в файл json
music_player.save_songlist("/Users/ersultanersultan/Desktop/Python/lap7/music/song.json")