import tools
import histogram
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Image Ecualizer")

image = Image.open("data/image.jpg")
image = ImageTk.PhotoImage(image)
image_label = tk.Label(window, image=image)
image_label.pack()

# Run
window.mainloop()

