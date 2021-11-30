import random
import os
from time import sleep
#shifting of array 

def shift(arr):
  for i in range(0,4):
    if arr[i]==0:
      a=arr.pop(i)
      arr.insert(0,a)
  i=0
  while i<3:
    if arr[i]==arr[i+1] and arr[i]!=0:
      arr[i+1]=2*arr[i]
      arr[i]=0
      i+=1
    i+=1
  for i in range(0,4):
    if arr[i]==0:
      a=arr.pop(i)
      arr.insert(0,a)
  return arr

#right push code

def rp(l):
  for i in range(0,4):
    a=l[4*i:(4*i+4)]
    a=shift(a)     
    l[4*i:(4*i+4)]=a
  return l

#left push code

def lp(l):
  for i in range(0,4):
    a=l[4*i:(4*i+4)]
    a.reverse()
    a=shift(a)
    a.reverse()
    l[4*i:(4*i+4)]=a
  return l

#code to push tiles down

def dp(l):
  for i in range(0,4):
    a=[l[i],l[i+4],l[i+8],l[i+12]]
    a=shift(a)
    [l[i],l[i+4],l[i+8],l[i+12]]=a
  return l

#code to push tiles up

def up(l):
  for i in range(0,4):
    a=[l[i],l[i+4],l[i+8],l[i+12]]
    a.reverse()
    a=shift(a)
    a.reverse()
    [l[i],l[i+4],l[i+8],l[i+12]]=a
  return l  

#code to print and display also clears the terminal

def show(l):
  n=len(str(max(l)))
  m=fox(l)
  print("1: Move left  2: Move right  3: Move up  4: Move down")
  for i in range(0,4):
    for j in range(0,4):
      if m[i][j]==0:
        m[i][j]='_'
      else:
        m[i][j]=str(m[i][j])
      while len(m[i][j])<n:
        m[i][j]=m[i][j]+' '
  for i in range(0,4):
    print(' '.join(m[i]))
  pass

# adds a new tile with 2

def newtile(L):
  e=[]
  for i in range(0,16):
    if L[i]==0:
      e.append(i)
  x=random.choice(e)
  L[x]=1024
  return L

# Generates 2 D array from linear array

def fox(L):
  mass=[[0 for i in range(0,4)] for j in range(0,4)]
  for i in range(0,16):
    mass[i//4][i%4]=L[i]
  return mass

#Main code from here
contvar=0
while contvar!=1:
  ls=[0 for i in range(0,16)]
  ls=newtile(ls)
  ls=newtile(ls)
  a=1
  while a==1:
    os.system('cls' if os.name == 'nt' else 'clear')
    show(ls)
    if 2048 in ls:
      a=2
      break
    if 0 not in ls:
      a=0
      break
    try:
      uinp=int(input())
    except ValueError:
      print('Invalid input. Please try again')
      sleep(2)
      continue
    if uinp<1 or uinp>4:
      print('Invalid input. Please try again')
      sleep(2)
      continue
    if uinp==1:
      ls=lp(ls)
    elif uinp==2:
      ls=rp(ls)
    elif uinp==3:
      ls=up(ls)
    elif uinp==4:
      ls=dp(ls)
    ls=newtile(ls)
  if a==0:
    print('Game over! You lost :(')
  elif a==2:
    print('Congratualtions, you have won! :)')
  print('Would you like to play again or quit?')
  contvar=input('1: Quit \nEnter any other input to play again\n')
  if contvar=='1':
    print('Thanks for playing!')
    contvar=1
  else:
    contvar=0