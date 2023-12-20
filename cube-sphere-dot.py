'''

	CubeSphere with dots
	github.com/RonAmerica/CubesIntoSpheres

'''


import tkinter as tk
import math
import time


def modAng(n):
 return (n+math.pi)%(2*math.pi)-math.pi


def stop():
 for i in range(c):
  vx[i]=0
  vy[i]=0
  vz[i]=0


def init():
 global c
 for x in range(n):
  for y in range(n):
   for z in range(n):
    if x==0 or x==h or y==0 or y==h or z==0 or z==h:
     c+=1
     cx.append(x-offset)
     cy.append(y-offset)
     cz.append(z-offset)
     vx.append(0)
     vy.append(0)
     vz.append(0)


def engage():
 global ft
 ft=400
 k=1/ft
 for i in range(c):
  dx=cx[i]
  dy=cy[i]
  dz=cz[i]
  m=offset*math.sqrt(2)/math.sqrt(dx*dx+dy*dy+dz*dz)
  vx[i]=k*(m*dx-cx[i])
  vy[i]=k*(m*dy-cy[i])
  vz[i]=k*(m*dz-cz[i])


def spinModel(t):
 global va,st,ft
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
  C.delete("dot")
  for i in range(c):
   dx=cx[i]-px
   dy=cy[i]-py
   dz=cz[i]-pz
   cx[i]+=vx[i]
   cy[i]+=vy[i]
   cz[i]+=vz[i]
   x=hw+zm*modAng(math.atan2(dx,dy)-va)
   y=hw+zm*modAng(math.atan2(dz,math.sqrt(dy*dy+dx*dx)))
   C.create_oval(x-1,y-1,x+1,y+1,outline="white",tags="dot")
  top.update()


def say(t,s):
 C.create_text(hw,25,fill="white",text=s,tags="tx")
 spinModel(t)
 C.delete("tx")


cx=[]
cy=[]
cz=[]

vx=[]
vy=[]
vz=[]

c=0
ft=0
st=0
va=0
pz=0

spin=0.003
w=600
hw=w/2
n=8
h=n-1
di=16
zm=8*hw/math.pi
offset=.5*(n-1)

top=tk.Tk()
top.title("Cubes Into Spheres")
C=tk.Canvas(top,bg="black",width=w,height=w)
C.pack()

init()

spinModel(2)

say(4,"Here is a cube.")

say(6,
 "Unlike a cube, all points on the surface of\n"
 "a sphere are the same distance from the center."
)

say(6,
 "So let's change our cube into a sphere\n"
 "by moving all the dots to the desired radius."
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


