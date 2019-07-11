module drawRay(p1,p2,width,height){ // draw ray between 2 specified points
    translate((p1+p2)/2)
    rotate([-acos((p2[2]-p1[2]) / norm(p1-p2)),0,
            -atan2(p2[0]-p1[0],p2[1]-p1[1])])
    cube([width,height,norm(p1-p2)+width], center = true);

} 


module Touch1D()
{
    phi = $t*360;
    x = 0;
    y = 0;
    crank_radius = 50.0;
    rod_length = 120.0;
    elements_height = 14;
    rod_width = 20;
      
    
    circle_radius = crank_radius + 7.5;
    
    //Base
    translate([-(crank_radius+7.5), -crank_radius-40, -elements_height]){
        cube([(2.5*crank_radius+rod_length),2*crank_radius+80,elements_height], center = false);
    }
    
    
    //Crank
    translate([x, y, 0]) {

        //1 Crank cylinder
        color([235/255, 227/255, 157/255],0.5)
        cylinder(h = elements_height, r = circle_radius, center = false);

        //3 Hinge pin
        translate([crank_radius*cos(phi),crank_radius*sin(phi),elements_height]){
            pin_radius = 5;
            pin_height = 10;
            color([66/255, 135/255, 245/255],1.0)
            cylinder(h = pin_height, r = pin_radius, center = false);
            //cube([]);
        }
        
    }
    
    slider_y = y;
    slider_x = x + crank_radius * cos(phi) + sqrt(rod_length*rod_length - (crank_radius*sin(phi))*(crank_radius*sin(phi)));
   
    slider_width = 20.0;
    slider_height = 40.0;  
    //5 slider
    translate([slider_x, slider_y, elements_height/2]) {

        cube([slider_width, slider_height, elements_height], center = true);
        
        //4 Hinge pin
        translate([0,0,elements_height/2]){
            pin_radius = 5;
            pin_height = 10;
            color([66/255, 135/255, 245/255],1.0)
            cylinder(h = pin_height, r = pin_radius, center = false);
        }
    }
    
    //2 Rod
    rod_offset = 1.5*elements_height;
    color([],0.5)
    drawRay([crank_radius*cos(phi),crank_radius*sin(phi),rod_offset],
             [slider_x,slider_y,rod_offset],
             width = rod_width, 
             height = elements_height);
    
    //Rails
    rails_begin = x + crank_radius * cos(180) + sqrt(rod_length*rod_length - (crank_radius*sin(180))*(crank_radius*sin(180)));
    rails_end = x + crank_radius * cos(0) + sqrt(rod_length*rod_length - (crank_radius*sin(0))*(crank_radius*sin(0)));
    rails_length = abs(rails_end - rails_begin);
    translate([rails_begin-slider_width/2,slider_height/2,0]) {
        cube([rails_length+slider_width,elements_height,elements_height],center = false);
    }
    translate([rails_begin-slider_width/2,-slider_height/2-elements_height,0]) {
        cube([rails_length+slider_width,elements_height,elements_height],center = false);
    }
    
    // Driver
    motor_radius = 5;
    translate([0,circle_radius+motor_radius,elements_height/2]) {
        cylinder(h = elements_height, r = motor_radius, center = true);
    }
    
    
    /*
    //Hinge pin
    translate(){
        pin_radius = 5;
        pin_height = 10;
        color([66/255, 135/255, 245/255],1.0)
        cylinder(h = pin_height, r = pin_radius, center = false);
    }*/

}

Touch1D();
