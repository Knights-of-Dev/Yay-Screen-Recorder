import tkinter as tk
import pyscreenrec

moniter = 1
framerate = 30
name = "recording.mp4"



#functions
def leave():
    root.destroy()

def minestartrecording():
    global moniter
    global framerate
    global name
    if framerate > 60:
        framerate = 60
    recorder.start_recording(str(name), int(framerate), {"mon": moniter})
    statetext.config(text="Recording")

def minestoprecording():
    if recorder.is_recording:
        recorder.stop_recording()
        statetext.config(text="Not Recording")

def minepauserecording():
    if recorder.is_recording and not recorder.is_paused:
        recorder.pause_recording()
        statetext.config(text="Paused")

def mineresumerecording():
    if recorder.is_paused:
        recorder.resume_recording()
        statetext.config(text="Recording")
        

#window set up / settings
root = tk.Tk()
root.title("Yay-Screen-Recorder")
root.geometry("200x200")

# pyscreenrec set up
recorder = pyscreenrec.ScreenRecorder()

#widgits being created
stop = tk.Button(root, command = minestoprecording, text = "Stop")
start = tk.Button(root, command = minestartrecording, text = "Start")
pause = tk.Button(root, command = minepauserecording, text = "Pause")
resume = tk.Button(root, command = mineresumerecording, text = "Resume")
statetext = tk.Label(root, text = "Not Recording")


#add widget to windows :3
start.place(x=0,y=0)
stop.place(x=0,y=25)
pause.place(x=0,y=50)
resume.place(x=0,y=75)
statetext.place(x=100,y=100)




root.mainloop()
