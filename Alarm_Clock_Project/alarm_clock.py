import pygame  #using for sound playback
import time    #usimng for real time countdown behaviour

pygame.mixer.init()  #initializing pygame's audio engine, without this, it'll give error

def alarm_clock(seconds):

    for time_left in range(seconds, -1, -1):  #range(startWith, stopAt, Updation) ->stop pnt is exlusive used -1, so it'll run till 0 sec 
        
        #converting seconds in minutes and seconds
        mins, secs = divmod(time_left , 60) #for finding min-left = time-left//60 , for sec-left = time-left%60
        
        #print timer on same line
        print(f"\rAlarms in: {mins:02d} : {secs:02d} ",end="") #end = "" is used in python it automatically shifts to newline and we want to print in the same line
        #\r for moving cursor back to beginning of the same line

        #executes after every 1 seconds
        time.sleep(1)

    print("\nTime's up!")    #reached 00:00 sec i.e timer completed

    pygame.mixer.music.load("alarm.mp3") #loading the audio file
    pygame.mixer.music.play()  #play the audio

    while pygame.mixer.music.get_busy(): #program runs till the sound plays
            time.sleep(1)   #check ones every seconds for audio

#taking input from user
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

total_seconds = minutes*60 + seconds  

alarm_clock(total_seconds) #alarm starts
