import cv2
import numpy as np
img=cv2.imread('output.png')

def getColors(x,y):
  ret=[]
  ret.append(img[y*3+2,x*2+2])
  ret.append(img[y*3+2,x*2+2+1])
  ret.append(img[y*3+2+1,x*2+2])
  ret.append(img[y*3+2+1,x*2+2+1])
  ret.append(img[y*3+2+2,x*2+2])
  ret.append(img[y*3+2+2,x*2+2+1])
  return ret

h,w,_=img.shape
maxX=(w-2)//2
maxY=(h-2)//3

blue=[255,0,0]
green=[0,255,0]
red=[0,0,255]
yellow=[0,255,255]
lblue=[255,255,0]
lred=[255,0,255]
white=[255,255,255]
black=[0,0,0]
gray=[128,128,128]

ca=[lred,red,green,yellow,blue,lblue]
cb=[red,lred,green,yellow,blue,lblue]
cc=[red,green,lred,yellow,blue,lblue]
cd=[red,green,yellow,lred,blue,lblue]
ce=[red,green,yellow,blue,lred,lblue]
cf=[red,green,yellow,blue,lblue,lred]
cg=[green,red,yellow,blue,lblue,lred]
ch=[green,yellow,red,blue,lblue,lred]
ci=[green,yellow,blue,red,lblue,lred]
cj=[green,yellow,blue,lblue,red,lred]
ck=[green,yellow,blue,lblue,lred,red]
cl=[yellow,green,blue,lblue,lred,red]
cm=[yellow,blue,green,lblue,lred,red]
cn=[yellow,blue,lblue,green,lred,red]
co=[yellow,blue,lblue,lred,green,red]
cp=[yellow,blue,lblue,lred,red,green]
cq=[blue,yellow,lblue,lred,red,green]
cr=[blue,lblue,yellow,lred,red,green]
cs=[blue,lblue,lred,yellow,red,green]
ct=[blue,lblue,lred,red,yellow,green]
cu=[blue,lblue,lred,red,green,yellow]
cv=[lblue,blue,lred,red,green,yellow]
cw=[lblue,lred,blue,red,green,yellow]
cx=[lblue,lred,red,blue,green,yellow]
cy=[lblue,lred,red,green,blue,yellow]
cz=[lblue,lred,red,green,yellow,blue]

chlist=[ca,cb,cc,cd,ce,cf,cg,ch,ci,cj,ck,cl,cm,cn,co,cp,cq,cr,cs,ct,cu,cv,cw,cx,cy,cz]

num0=[black,gray,white,black,gray,white]

num1=[gray,black,white,black,gray,white]
num2=[gray,white,black,black,gray,white]
num3=[gray,white,black,gray,black,white]
num4=[gray,white,black,gray,white,black]
num5=[white,gray,black,gray,white,black]
num6=[white,black,gray,gray,white,black]
num7=[white,black,gray,white,gray,black]
num8=[white,black,gray,white,black,gray]
num9=[black,white,gray,white,black,gray]
nums=[num0,num1,num2,num3,num4,num5,num6,num7,num8,num9]

comma=[white,black,black,white,white,black]
period=[black,white,white,black,black,white]
blank=[white,white,white,white,white,white]
def check(checkarray,template):
  for i in range(6):
    if not (checkarray[i]==template[i]).all():
      return False
  return True

for y in range(maxY):
  print('')
  for x in range(maxX):
    for i,ch in enumerate(chlist):
      if check(getColors(x,y),ch):
        print(chr(97+i),end='')
      if check(getColors(x,y),blank):
        print(' ',end='')
        break
    for i in range(10):
      if check(getColors(x,y),nums[i]):
        print(i,end='')
    if check(getColors(x,y),comma):
      print(',',end='')
    if check(getColors(x,y),period):
      print('.',end='')
