import turtle as ttl
class circle(object):
    def __init__(self,r,color):
        self.r=r
        self.color=color
    
    def drawc(self):
        ttl.circle(self.r,self.color)
        
c1=circle(50,"red")
c1.drawc()
