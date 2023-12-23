'''

	CubeSphere in OpenGL
	github.com/RonAmerica/CubesIntoSpheres

'''

import math

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window=0
angle=0
width,height=640,640
dist=8
tt=200
mv=tt
tv=[]

vt=[
 -1,-1,1,	1,-1,1,		1,1,1,		-1,1,1,
 -1,-1,-1,	1,-1,-1,	1,1,-1,		-1,1,-1,
 1,-1,1,	1,1,1,		1,1,-1,		1,-1,-1,
 -1,-1,1,	-1,1,1,		-1,1,-1,	-1,-1,-1,
 -1,1,1,	1,1,1,		1,1,-1,		-1,1,-1,
 -1,-1,1,	1,-1,1,		1,-1,-1,	-1,-1,-1,
]

color=(
 1,0,0,
 0,1,0,
 0,0,1,
 1,0,1,
 1,1,0,
 0,1,1,
)


def copyV(i):
 vt.append(vt[i])
 vt.append(vt[i+1])
 vt.append(vt[i+2])

def tweenV(a,b):
 vt.append(.5*(vt[a]+vt[b]))
 vt.append(.5*(vt[a+1]+vt[b+1]))
 vt.append(.5*(vt[a+2]+vt[b+2]))

def divide(i):
 i*=12
 copyV(i)
 tweenV(i,i+3)
 tweenV(i+3,i+9)
 tweenV(i,i+9)
 tweenV(i,i+3)
 copyV(i+3)
 tweenV(i+3,i+6)
 tweenV(i+3,i+9)
 tweenV(i+3,i+9)
 tweenV(i+3,i+6)
 copyV(i+6)
 tweenV(i+6,i+9)
 tweenV(i,i+9)
 tweenV(i+3,i+9)
 tweenV(i+6,i+9)
 copyV(i+9)
 vt[i:i+12]=[]

def draw():
 global angle,dist,mv
 angle+=.01
 x=dist*math.sin(angle)
 y=dist*math.cos(angle)
 glPushMatrix()
 gluLookAt(x,0,y, 0,0,0, 0,1,0)
 glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
 if mv>0:
  i=0
  while i<len(vt):
   vt[i]+=tv[i]
   i+=1
  mv-=1
  if mv==0:
   reverse()
   mv=tt
 glBegin(GL_QUADS)
 i=0
 while i<len(vt):
  c=(int(i/12)%6)*3
  glColor3f(color[c],color[c+1],color[c+2])
  glVertex3f(vt[i],vt[i+1],vt[i+2])
  glVertex3f(vt[i+3],vt[i+4],vt[i+5])
  glVertex3f(vt[i+6],vt[i+7],vt[i+8])
  glVertex3f(vt[i+9],vt[i+10],vt[i+11])
  i+=12;
 glEnd()
 glutSwapBuffers()
 glPopMatrix()

def reverse():
 for i in range(len(vt)):
  tv[i]=-tv[i]


i=0
while i<len(vt):
 dx=vt[i]-vt[i+6]
 dy=vt[i+1]-vt[i+7]
 dz=vt[i+2]-vt[i+8]
 di=math.sqrt(dx*dx+dy*dy+dz*dz)
 if di>.7:
  divide(i)
 else:
  i+=12


for i in range(0,len(vt),3):
 dx=vt[i]
 dy=vt[i+1]
 dz=vt[i+2]
 di=math.sqrt(dx*dx+dy*dy+dz*dz)
 m=(6/math.pi)**(1/3)/di
 dx*=m
 dy*=m
 dz*=m
 m=1/tt
 vx=m*(dx-vt[i])
 vy=m*(dy-vt[i+1])
 vz=m*(dz-vt[i+2])
 tv.append(vx)
 tv.append(vy)
 tv.append(vz)


glutInit()
glutInitDisplayMode(GLUT_DOUBLE|GLUT_DEPTH)
glutInitWindowSize(width,height)
glutInitWindowPosition(0,0)
window=glutCreateWindow("Cubes Into Spheres")
gluPerspective(25,width/height,1,80)
glEnable(GL_DEPTH_TEST)
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()


