﻿# Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.

import pygame
import time

pygame.init()
pygame.mixer.music.load('../Midia/audio_teste.mp3')
pygame.mixer.music.play()

time.sleep(20)