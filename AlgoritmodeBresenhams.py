##BresenhamDraw a circle
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import animation
import random as rd
# ==========================================
# Round basic information
# 1. Circle radius
r = 6.0
# 2. Circle center coordinates
a, b = (0., 0.)
Ary=[]
Aryd=[]
# ==========================================
##Bresenham method of calculating points
##Drawing point direction Only the lower right L point or the right H point
##Calculate D(H) D(L) The calculation formula is D(p)=px*px+py*py-r*r
##Calculate di=D(H)+D(L) di>0 then draw L, di<=0 then draw H
##Consider the symmetry of the circle and draw (x, y), (-x, y), (-x, -y), (x, -y), (y, x), (- y,x),(-y,-x),(y,-x) eight points
##Start and end positions (0,r) to (r-1,y), because there is no good way to judge the end point
##In order to fit most radii, we still use the end point above, although it will draw a few more points, but it consumes little
##def init():
##    plt.set_xlim(Ary[

def getPoint():
    R=int(r)
    st=[0,R]
    Ary.append(st)
    plt.scatter(0,R,color='b')
    plt.scatter(0,-R,color='b')
    plt.scatter(-R,0,color='b')
    plt.scatter(R,0,color='b')
    for i in range(0,R-1):
        H=[st[0]+1,st[1]]
        L=[st[0]+1,st[1]-1]
        DH=H[0]*H[0]+H[1]*H[1]-R*R
        DL=L[0]*L[0]+L[1]*L[1]-R*R
        di=DH+DL
        Aryd.append(di)
        if(di>0):
            H=L
        st=H
        Ary.append(st)
        DrawPoint(st[0],st[1],'b')

def DrawPoint(x,y,cr):
    plt.scatter(x,y,color=cr)
    plt.scatter(-x,y,color=cr)
    plt.scatter(-x,-y,color=cr)
    plt.scatter(x,-y,color=cr)
    plt.scatter(y,x,color=cr)
    plt.scatter(-y,x,color=cr)
    plt.scatter(-y,-x,color=cr)
    plt.scatter(y,-x,color=cr)
    
def setAxis():
    lent=range(-15,15,1)
    plt.xticks(lent)
    plt.yticks(lent)
    plt.plot([-18,18],[0,0],'k')
    plt.plot([0,0],[-18,18],'k')
##Parametric equation drawing circle
def drawCle():
    theta = np.arange(0, 2*np.pi, 0.01)
    x = a + r * np.cos(theta)
    y = b + r * np.sin(theta)
    plt.plot(x,y,'r')
    plt.axis('equal')
    
##plt.show()

if  __name__=="__main__":
##    r=float(input("r:"))
    r=int(rd.uniform(3,15)+0.5)
##    r=8
    setAxis()
    getPoint()
    drawCle()
    print(Ary)
    print(Aryd)
    plt.show() 