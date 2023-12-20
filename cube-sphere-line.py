'''

	CubeSphere with lines
	github.com/RonAmerica/CubesIntoSpheres

'''

import tkinter as tk
import math
import time


class Dot:
 vx=0
 vy=0
 vz=0
 px=0
 py=0
 def __init__(self,x,y,z):
  self.x=x
  self.y=y
  self.z=z
  self.link=[]


def modAng(n):
 return (n+math.pi)%(2*math.pi)-math.pi


def getXY(d):
 global px,py
 dx=d.x-px
 dy=d.y-py
 dz=d.z-pz
 x=hw+zm*modAng(math.atan2(dx,dy)-va)
 y=hw+zm*modAng(math.atan2(dz,math.sqrt(dy*dy+dx*dx)))
 return x,y


def stop():
 for i in range(c):
  dot[i].vx=0
  dot[i].vy=0
  dot[i].vz=0


def init():
 global c
 for x in range(n):
  for y in range(n):
   for z in range(n):
    if x==0 or x==h or y==0 or y==h or z==0 or z==h:
     dot.append(Dot(x-offset,y-offset,z-offset))
 c=len(dot)


def link():
 for i in range(c-1):
  for j in range(i+1,c):
   dx=dot[i].x-dot[j].x
   dy=dot[i].y-dot[j].y
   dz=dot[i].z-dot[j].z
   dd=dx*dx+dy*dy+dz*dz
   if dd<1.1:
    dot[i].link.append(j)


def engage():
 global ft
 ft=200
 k=1/ft
 for i in range(c):
  dx=dot[i].x
  dy=dot[i].y
  dz=dot[i].z
  m=offset*math.sqrt(2)/math.sqrt(dx*dx+dy*dy+dz*dz)
  dot[i].vx=k*(m*dx-dot[i].x)
  dot[i].vy=k*(m*dy-dot[i].y)
  dot[i].vz=k*(m*dz-dot[i].z)


def spinModel(t):
 global va,st,ft,px,py
 while t:
  ct=int(time.time())
  if t>0 and ct!=st:
   st=ct
   t-=1
  if ft>0:
   ft-=1
   if not ft:
    t=0
  va+=spin
  va%=2*math.pi
  px=-math.sin(va)*di
  py=-math.cos(va)*di
  C.delete("sphere")
  for i in range(c):
   dot[i].x+=dot[i].vx
   dot[i].y+=dot[i].vy
   dot[i].z+=dot[i].vz
   x1,y1=getXY(dot[i])
   for j in range(len(dot[i].link)):
    x2,y2=getXY(dot[dot[i].link[j]])
    cc=(i^j)%len(color)
    C.create_line(x1,y1,x2,y2,fill=color[cc],tags="sphere")
  top.update()


def say(t,s):
 C.create_text(hw,28,fill="white",font=('Sans-serif',16),text=s,tags="tx")
 spinModel(t)
 C.delete("tx")


color=["#f00","#0f0","#00f","#ff0","#0ff","#f0f"]

c=0
ft=0
st=0
va=0
pz=0

dot=[]

spin=0.003
w=600
hw=w/2
n=4
h=n-1
di=16
zm=18*hw/math.pi
offset=.5*(n-1)

top=tk.Tk()
top.title("Cubes Into Spheres")
C=tk.Canvas(top,bg="black",width=w,height=w)
C.pack()

init()
link()

spinModel(2)

say(4,"Here is a cube.")

say(6,
 "Unlike a cube, all points on the surface of\n"
 "a sphere are the same distance from the center."
)

say(6,
 "So let's change our cube into a sphere\n"
 "by moving all vertices to the desired radius."
)

engage()
say(999,"Watch closely!")

stop()
say(4,"Now we have a sphere!")

say(8,
 "This is better than drawing it by latitude & longitude,\n"
 "with wasteful excess detail at the poles."
)

say(5,"CubeSpheres are rounder for the same resources.")

spinModel(-1)


