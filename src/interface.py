import tkinter as tk
import ttkthemes as ttk
import customtkinter as ctk
import numpy as np
import math
from imageWidget import *
from PIL import Image, ImageTk
from menu import Menu
from tools import *

class App(ctk.CTk):
    def __init__(self):
        # Setup
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.geometry("1000x600")
        self.title("Image Equalizer")
        self.minsize(800,500)
        self.init_parameters()
        # layout
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight  = 2, uniform = "a")
        self.columnconfigure(1, weight = 6, uniform = "a")

        # Canvas data
        self.image_width = 0
        self.image_height = 0
        self.canvas_width = 0
        self.canvas_heigth = 0

        #ImageImport
        self.image_import = ImageImport(self, self.import_image)
        # Run
        self.mainloop()

    def init_parameters(self):
        self.options = ctk.StringVar(value = OPTIONS[0]) 
        self.options.trace("w", self.manipulate_image) 
        self.quantized_value = ctk.IntVar(value = QUANTIZED_VALUE)
        self.quantized_value.trace("w",self.manipulate_image)

    def manipulate_image(self, *args):
        self.image = read_image(np.array(self.original).astype("uint8"))
        q = math.floor(self.quantized_value.get())
        quantize_image = quantize(self.image,q,8).astype("uint8") 
        self.image = Image.fromarray(histogram_equalization(quantize_image,q)) 
        if self.options == "Image":
            # Placing the image
            self.place_image()
        elif self.options == "Histogram":
            self.image = graph(read_image(np.array(self.image).astype("uint8")),q)
            self.place_image()
        else:
            original =read_image(np.array(self.original).astype("uint8"))
            self.image = Image.fromarray(comparison(original,self.image))
            self.place_image()

    # Import Image
    def import_image(self,path):
        self.original = Image.open(path)
        self.image = self.original
        self.image_ratio = self.image.size[0] / self.image.size[1]

        self.image_tk = ImageTk.PhotoImage(self.image)
        self.image_import.grid_forget()
        self.image_output = ImageOutput(self,self.resize_image)

        self.close_button = CloseOutput(self,self.close_edit)
        self.menu = Menu(self, self.quantized_value, self.options, self.callback)

    def callback(self,choice):
        self.options = choice

    def close_edit(self):
        self.image_output.grid_forget()
        self.close_button.place_forget()
        self.menu.grid_forget()
        self.image_import = ImageImport(self,self.import_image)

    def resize_image(self, event):
        canvas_ratio = event.width / event.height
        self.canvas_width = event.width
        self.canvas_heigth = event.height
        if canvas_ratio > self.image_ratio:
            self.image_height = int(event.height)
            self.image_width = int(self.image_height * self.image_ratio)
        else:
            self.image_width = int(event.width)
            self.image_height = int(self.image_width / self.image_ratio)
        self.place_image()

    def place_image(self):
        # Place image
        self.image_output.delete("all")
        resize_image = self.image.resize((self.image_width,self.image_height))
        self.image_tk = ImageTk.PhotoImage(resize_image)
        self.image_output.create_image(self.canvas_width / 2,self.canvas_heigth / 2, image = self.image_tk)


# Run the app
App()
