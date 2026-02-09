import tkinter as tk
import pyscreenrec
import mss

moniter = 1
framerate = 30
name = "recording.mp4"
recording = False
paused = False



#functions
def leave():
    root.destroy()

def minestartrecording():
    global moniter
    global framerate
    global name
    global recording
    global paused
    global recorder

    if recording:
        return
    
    name2 = str(name)
    name2 = f"videos/{name2}"
    with mss.mss() as sct:
        mon = sct.monitors[moniter]
    
    if framerate > 60:
        framerate = 60
    recorder.start_recording(str(name2), int(framerate), mon)
    statetext.config(text="Recording")
    recording = True
    paused = False


def minestoprecording():
    global recording
    global paused
    global recorder
    if recording:
        recorder.stop_recording()
        statetext.config(text="Not Recording")
        recording = False
        paused = False

def minepauserecording():
    global recording
    global paused
    global recorder
    if recording and not paused:
        recorder.pause_recording()
        statetext.config(text="Paused")
        paused = True

def mineresumerecording():
    global recording
    global paused
    global recorder
    if paused:
        recorder.resume_recording()
        statetext.config(text="Recording")
        paused = False
        

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
