#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:21:58 2019

@author: Maksym Tymkovych
"""

from Tkinter import Frame, Canvas, Tk

from views import SliderCrankView
from models import SliderCrankModel
import time
import random

class Application(Frame):
    
    def __init__(self, parent, model):
        Frame.__init__(self,parent)
        self.parent = parent
        self.WIDTH = 400
        self.HEIGHT = 400
        self.initUI()
        self.view = SliderCrankView(model)
        self.animated = False
        print(self.view.model.getSliderPositionDistance())
        self.draw()
        pass
    
    def initUI(self):
        self.parent.title("Touch1D")
        self.canvas = Canvas(self.parent, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack();
        self.parent.bind("<Key>", self.key_press)
        pass
    
    def key_press(self, event):
        print event.char
        if event.char == " ":
            if self.animated == False:
                self.animated = True
                self.animate()
            else:
                self.animated = False
        if event.char == "a":
            
            self.view.model.phi = self.view.model.phi - 0.01  
            
        if event.char == "d":
            self.view.model.phi = self.view.model.phi + 0.01
            
        self.draw()
        pass
    
    def draw(self):
        self.view.draw(self.canvas)
        pass
    
    def animate(self):
        #TODO: random should be raplced by reading from sensor
        if not self.animated:
            return
        self.view.model.phi = self.view.model.phi - random.random()/10 
        self.draw()
        self.parent.after(200, self.animate)
        pass
    
    
def main():
    root = Tk()
    model = SliderCrankModel(50.0,120.0)
    model.x = 100
    model.y = 100
    Application(root, model)
    root.mainloop()
    pass

if __name__ == "__main__":
    main()