#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 00:35:46 2019

@author: montaindeveloper
"""

from Tkinter import Canvas
from models import SliderCrankModel

from math import pi, sin, cos, sqrt

class SliderCrankView:
    def __init__(self, model):
        self.model= model
        pass
    
    def draw(self, canvas):
        canvas.delete("all")
        
        
        driving_shaft_radius = 5
        
        canvas.create_oval(self.model.x - driving_shaft_radius, 
                           self.model.y - driving_shaft_radius, 
                           self.model.x + driving_shaft_radius, 
                           self.model.y + driving_shaft_radius, width=1.0)
        
        canvas.create_oval(self.model.x - self.model.crank_length, 
                           self.model.y - self.model.crank_length, 
                           self.model.x + self.model.crank_length, 
                           self.model.y + self.model.crank_length, width=1.0)
        
        hinge_pin_radius = 5
        
        slider_x = self.model.getSliderPosition()
        slider_y = self.model.y

        

        
        rod_start_x = self.model.x + self.model.crank_length*cos(self.model.phi)
        rod_start_y = self.model.y + self.model.crank_length*sin(self.model.phi)
        

        
        slider_width = 20
        slider_height = 40
        
        canvas.create_rectangle(slider_x - slider_width/2,
                                slider_y - slider_height/2,
                                slider_x + slider_width/2,
                                slider_y + slider_height/2,width=1.0,fill="green")
        
        slider_start_x, slider_finish_x = self.model.getSliderPositionRange()
        
        canvas.create_rectangle(slider_start_x - slider_width/2,
                                slider_y - slider_height/2,
                                slider_finish_x + slider_width/2,
                                slider_y - slider_height,width=1.0,fill="gray")
        
        canvas.create_rectangle(slider_start_x - slider_width/2,
                                slider_y + slider_height/2,
                                slider_finish_x + slider_width/2,
                                slider_y + slider_height,width=1.0,fill="gray")
        
        canvas.create_line(self.model.x,
                           self.model.y,
                           slider_x,
                           slider_y, dash=(4, 4))
        
        canvas.create_oval(slider_x - hinge_pin_radius, 
                           slider_y - hinge_pin_radius, 
                           slider_x + hinge_pin_radius, 
                           slider_y + hinge_pin_radius, width=1.0)
        
        canvas.create_oval(rod_start_x - hinge_pin_radius, 
                           rod_start_y - hinge_pin_radius, 
                           rod_start_x + hinge_pin_radius, 
                           rod_start_y + hinge_pin_radius, width=1.0)
        
        canvas.create_line(self.model.x,
                           self.model.y,
                           rod_start_x,
                           rod_start_y, width=1.0)
        
        canvas.create_line(rod_start_x,
                           rod_start_y, 
                           slider_x,
                           slider_y, width=1.0)
        
        pass
    
    
if __name__ == "__main__":
    
    print("Test")