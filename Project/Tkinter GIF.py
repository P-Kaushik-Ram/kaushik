import tkinter as tk
from PIL import Image

root = tk.Tk()
root.geometry("500x288")
root.title("MAIN MENU")

file="a.gif"

info = Image.open(file)

frames = info.n_frames

im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None
def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = root.after(50,lambda :animation(count))

gif_label = tk.Label(root, text='test',image="")
gif_label.pack()
animation(count)
root.mainloop()
