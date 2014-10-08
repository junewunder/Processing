

class Laser(object):
    def __init__(self,defx,defy,defr,angle):
        #self.defx = defx
        #self.defy = defy
        self.angle = angle
        
        self.x0 = defx + defr * cos(angle)
        self.y0 = defy + defr * sin(angle)
        self.x1 = defx + (defr+15) * cos(angle)
        self.y1 = defy + (defr+15) * sin(angle)
        
    def update(self):
        stroke(120,255,120)
        line(self.x0,self.y0,self.x1,self.y1)
        
        self.x0 += cos(self.angle)
        self.y0 += sin(self.angle)
        self.x1 += cos(self.angle)
        self.y1 += sin(self.angle)
        
        