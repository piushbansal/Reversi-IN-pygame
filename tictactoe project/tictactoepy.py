import pygame,sys,random,time
from pygame.locals import*
import tictactoemini2

pygame.init()

width = 300
height = 300
window= pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption('tictactoe')

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
font = pygame.font.SysFont('Gabriola',40)

my = []
for i in range(3):
  my.append([]*3)

#print my
size = 100
for i in range(3):
  for j in range(3):
    rect = pygame.Rect(i*size,j*size,size,size)
    my[i].append({'rect':rect,'colour':white})
    pygame.draw.rect(window,my[i][j]['colour'],rect)
    pygame.draw.line(window,blue,(0,size*j),(width,size*j))
  pygame.draw.line(window,blue,(i*size,0),(size*i,height))

def isptinsiderect(pos, rect):
  if (pos.x > rect.left) and (pos.x < rect.right) and (pos.y > rect.top) and (pos.y <rect.bottom):
    return True

def haha(k):
  list1 = [[2,0],[1,0],[0,0],[2,1],[1,1],[0,1],[2,2],[1,2],[0,2]]
  for i in range(len(list1)):
    if list1[i]==k:
      return 9-i-1

def printtxt(s):
  list1 = [[2,0],[1,0],[0,0],[2,1],[1,1],[0,1],[2,2],[1,2],[0,2]]
  for i in range(len(s)):
    txt = font.render(what(s[i]),True,black)
    txtrect = txt.get_rect()
    txtrect.centerx=my[list1[8-i][0]][list1[8-i][1]]['rect'].centerx
    txtrect.centery = my[list1[8-i][0]][list1[8-i][1]]['rect'].centery
    window.blit(txt,txtrect)
s = [' ']*9
def change_in_s(s,index):
  if s[index]==' ':
    s[index]=1
    return 1
  return 0
def what(p):
  if p==-1:
    return 'o'
  if p==1:
    return 'x'
  return p
print(s[0])
list1 = [[2,0],[1,0],[0,0],[2,1],[1,1],[0,1],[2,2],[1,2],[0,2]]
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type ==MOUSEBUTTONDOWN:
      for i in range(3):
        for j in range(3):
          if isptinsiderect(event.pos,my[i][j]['rect']):
            k = [i,j]
            #print k
            #print(haha(k))
            if change_in_s(s,haha(k)):
             # print s
              printtxt(s)
              pygame.display.flip()
              if tictactoemini2.iswinning(s,1):
                  txt1 = 'you win'
                  break
              if tictactoemini2.iswinning(s,-1):
                  txt1 = 'i win'
                  break
              if len(tictactoemini2.newlist1(s))==0:
                  txt1 = 'match draw'
                  break
              s = tictactoemini2.compreturns(s,6,-1)
  printtxt(s)
  pygame.display.flip()
  if tictactoemini2.iswinning(s,1):
    txt1 = 'you win'
    break
  if tictactoemini2.iswinning(s,-1):
    txt1 = 'i win'
    break
  if len(tictactoemini2.newlist1(s))==0:
    txt1 = 'match draw'
    break
time.sleep(0.2)
window2 = pygame.display.set_mode((300,100),0,32)
pygame.display.set_caption('result')
window2.fill(white)
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  font1 = pygame.font.SysFont('comic sans ms',30)
  txt3 = font1.render(txt1,True,blue)
  txt3rect = txt3.get_rect()
  txt3rect.centerx = 150
  txt3rect.centery = 50
  window2.blit(txt3,txt3rect)
  pygame.display.flip()
