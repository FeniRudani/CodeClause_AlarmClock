from tkinter import *
from tkinter import messagebox
import time,sys
from pygame import mixer
from PIL import Image, ImageTk

def alarm():
    alarm_time = user_input.get()
    if alarm_time == "":
        messagebox.askretrycancel("Error Message", "Please Enter Value")

    else:
        while True:
            time.sleep(1)
            if(alarm_time==time.strftime("%H:%M")):
                playmusic() 

def playmusic():
    mixer.init()
    mixer.music.load("AlarmSound.mp3")
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(30)
        mixer.music.stop()
        sys.exit()                   





root = Tk()
root.title("Alarm Clock")
window_width = 889
window_height = 500
canvas = Canvas(root, width=window_width, height=window_height)
Photo = Image.open("alarmClock.webp")
image = ImageTk.PhotoImage(Photo)
canvas.create_image(0,0,anchor = NW, image = image)
canvas.pack()
header = Frame(root)
heading = Frame(root)

box1 = Frame(root)
box1.place(x=650, y= 180)
box2= Frame(root)
box2.place(x= 650 , y=260)

user_input = Entry(box1, font=("Ariel Narorow", 20), width = 8)
user_input.grid(row = 0, column = 2)

start_button = Button(box2, text="Set Alarm", font = ("Ariel Narrow", 16,"bold"), command = alarm)
start_button.grid(row =2, column=2)

root.mainloop()