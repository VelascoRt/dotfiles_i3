import customtkinter as ctk
from panels import *

class Menu(ctk.CTkTabview):
    def __init__(self,parent,quantized,options):
        super().__init__(master = parent)
        self.grid(row = 0, column = 0, sticky = "nsew")
        
        self.add("Equalizer")
        self.add("Comparison")

        EqualizerFrame(self.tab("Equalizer"),quantized)
        ComparisonFrame(self.tab("Comparison"),options)

class EqualizerFrame(ctk.CTkFrame):
    def __init__(self,parent,quantized):
        super().__init__(master = parent, fg_color = "transparent")
        self.pack(expand = True, fill = "both")

        SliderPanel(self,"Quantized Value", quantized, 1, 8)

class ComparisonFrame(ctk.CTkFrame):
    def __init__(self,parent,options):
        super().__init__(master = parent)
        self.pack(expand = True, fill = "both")
        DropDownPanel(self,options["image"],["Image","Histogram","Comparison","Acumulative Histogram"])
      
