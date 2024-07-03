import pygame
import os
import time

pygame.init()
songs = [
    [" ",4],
    ["ช่วยเดินไปบอกเขาเลย ว่าฉันไม่ให้ไป",6.5],
    ["แล้วก็ตอบเขาที ว่าฉันยังมีความหมาย",7],
    ["เพราะเขาแค่เข้ามา ทำให้เธอหวั่นไหว",6.5],
    ["มันไม่ใช่เรื่องจริง จากนี้ไม่ต้องวุ่นวายกันอีก",8],
    ]
music_path = os.path.join(os.getcwd(),  'lyric', 'song1.mp3')
pygame.mixer.music.load(music_path)

pygame.mixer.music.play()

running = True
while running:
    for x in songs :
        print(x[0])
        print()
        time.sleep(x[1])
        
    
        
pygame.quit()
