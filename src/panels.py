import customtkinter as ctk
import math
from settings import *

class Panel(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(master = parent, fg_color = DARK_GREY)
        self.pack(fill = "x", pady = 4, ipady = 8)

class SwitchPanel(Panel):
    def __init__(self,parent,*args):
        super().__init__(parent = parent)
        for var,text in args:
            switch = ctk.CTkSwitch(self,text=text,variable = var,button_color = BLUE,fg_color=SLIDER_BG)
            switch.pack(side="left",expand=True,fill="both",padx=5,pady=5)

class SliderPanel(Panel):
    def __init__(self,parent,text,quantized, min_value, max_value):
        super().__init__(parent = parent)

        self.rowconfigure((0,1), weight = 1)
        self.columnconfigure((0,1), weight = 1)

        ctk.CTkLabel(self, text = text).grid(column = 0, row = 0, sticky = "W", padx = 5)
        self.num_label = ctk.CTkLabel(self, text = quantized.get())
        self.num_label.grid(column = 1, row = 0, sticky = "E", padx = 5)

        ctk.CTkSlider(self, 
                      fg_color = SLIDER_BG, 
                      variable = quantized,
                      from_ = min_value,
                      to = max_value,
                      command = self.update_text).grid(column = 0, row = 1, columnspan=2,sticky="ew",padx=5,pady=5)
    def update_text(self,value):
        self.num_label.configure(text = f"{math.floor(value)}")
