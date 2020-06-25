from json import load
from pynput.mouse import Controller as mouse, Button as b
from pynput.keyboard import Controller as keyboard
from pynput.keyboard import Key
from time import sleep
from tkinter import *
from tkinter.messagebox import askokcancel

keyboard = keyboard()
mouse = mouse()


# First Monitor: Point(x=855, y=997)
# Second Monitor: Point(x=2745, y=997)
def center_window(w, h):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

def getNames(filename):
    with open(filename, "r") as f:
        return load(f)
def checkHours(names, timeToSleep):
    checking.config(text="Checking...")
    startButton.config(state=DISABLED)
    root.update_idletasks()
    for discord_id in names["names"]:
        checking.pack(pady=20)
        mouse.position = (2745, 997)
        mouse.click(b.left, 1)
        keyboard.type(f"--rank <@{discord_id}>")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        sleep(timeToSleep)
    checking.config(text="Done!")
    startButton.config(state=NORMAL)

def isReady():
    ok = askokcancel(message='WARNING! Your Discord must be on the SECOND SCREEN in FULL SCREEN MODE, IN THE #RANK-CHECK CHAT')
    if ok:
        checkHours(getNames("names.json"), 2)

root = Tk()
root.iconbitmap("images//icon.ico")
center_window(600, 400)
root.title("Hour Checker for AlonDaPro")

font = ("Helvetica", 26, "bold")
startButton = Button(root, text="Start Checking!", command=isReady, width=20, height=3, bg='#3DADC8')
startButton.pack(pady=30)
checking = Label(root, text="Press the button to start checking!", font=font)
checking.pack(pady=70)

alon_image = PhotoImage(file="images//alon.png")
alon_label = Label(root, image=alon_image, width=150, height=150)
alon_label.place(x=450, y=0)

df = Label(root, text="Don't forget to warn whoever did less than 1 hour!", font=("Helvetica", 18), fg="#DC2828")
df.pack(pady=20)
tm = Label(root, text="Made by xYarin", font=('helvetica', 12, "underline"))
tm.place(x=5, y=0)

root.mainloop()
