import pygame,sys,time,random
from pygame.locals import *
import reversim2

pygame.init()
clock = pygame.time.Clock()
size = 70
width = 8*size
height = 8*size
window = pygame.display.set_mode((width,height+50),0,32)

pygame.display.set_caption('reversi')
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (40,250,40)
font  = pygame.font.SysFont('Gabriola',30)
font1 = pygame.font.SysFont('Gabriola',60)
my = []
for i in range(8):
  my.append([]*8)

for i in range(8):
  for j in range(8):
    rect = pygame.Rect(i*size,j*size,size,size)
    my[i].append({'rect':rect,'colour':green})
    pygame.draw.rect(window,my[i][j]['colour'],rect)
    pygame.draw.line(window,blue,(0,size*j),(width,size*j))
  pygame.draw.line(window,blue,(i*size,0),(size*i,height))
pygame.display.flip()
def isptinsiderect((x, y), rect):
  if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y <rect.bottom):
    return True
def printboard(board):
  for i in range(8):
    for j in range(8):
      if board[i][j] == -1:
        circlex = my[i][j]['rect'].centerx
        circley = my[i][j]['rect'].centery
        pygame.draw.circle(window,black,(circlex,circley),30,0)
      if board[i][j] == 1:
        circlex = my[i][j]['rect'].centerx
        circley = my[i][j]['rect'].centery
        pygame.draw.circle(window,white,(circlex,circley),30,0)
      if board[i][j]=='.':
        circlex = my[i][j]['rect'].centerx
        circley = my[i][j]['rect'].centery
        pygame.draw.circle(window,blue,(circlex,circley),6,2)

def moveuser(user,board,i_playernum):
  #global usermode
  #print validlist(i_playernum,-i_playernum,board)
  if (int(user[0]),int(user[1])) in reversim2.validlist(i_playernum,-i_playernum,board):
    #print 'here2'
    return reversim2.changes(board,i_playernum,-i_playernum,int(user[0]),int(user[1]))
  else :
    return board
board = reversim2.newboard()
printboard(board)
i_curplayer=1
i_depth = 3
board1= reversim2.hints(board,i_curplayer,-i_curplayer)
txt5 = font.render('undo',True,black)
txt5rect = txt5.get_rect()
txt5rect.centerx = width/2+150
txt5rect.centery = height+30
previous = []
previous.append(board)
running1 = True
running2 = True
txt10 = font1.render('press space to see the board ',True,blue)
txt10rect = txt10.get_rect()
txt11 = font.render('press space to end this',True,blue)
txt11rect = txt11.get_rect()
txt11rect.centerx = width/2
txt11rect.centery = height+25
while running2:
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == KEYUP:
      if event.key == K_ESCAPE:
          pygame.quit()
          sys.exit()
      if event.key == ord('a'):
        print 'here'
        window = pygame.display.set_mode((width,height+50),0,32)
        board = reversim2.newboard()
        printboard(board)
        i_curplayer=1
        i_depth = 3
        board1= reversim2.hints(board,i_curplayer,-i_curplayer)
        txt5 = font.render('undo',True,black)
        txt5rect = txt5.get_rect()
        txt5rect.centerx = width/2+150
        txt5rect.centery = height+30
        previous = []
        previous.append(board)
        running1 = True
        #running2 = False
      if event.key == K_SPACE:
        print'here2'
        window = pygame.display.set_mode((width,height+50),0,32)
        window.fill(white)
        for i in range(8):
          for j in range(8):
            pygame.draw.rect(window,my[i][j]['colour'],my[i][j]['rect'])
            pygame.draw.line(window,blue,(0,size*j),(width,size*j))
            pygame.draw.line(window,blue,(i*size,0),(size*i,height))
          pygame.draw.line(window,blue,(0,height),(width,height))
        printboard(board1)
        txt1 = 'your score = '+str(reversim2.sumpl(1,board))
        txt2 = 'my score = '+str(reversim2.sumpl(-1,board))
        txt3 = font.render(txt1+' , '+txt2,True,blue)
        txt3rect = txt3.get_rect()
        txt3rect.centerx = width/2-130
        txt3rect.centery = height+10
        window.blit(txt3,txt3rect)
        window.blit(txt11,txt11rect)
        pygame.display.update()
        running3 = True
        while running3:
          for event in pygame.event.get():
            if event.type == KEYUP:
              if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
              if event.key==K_SPACE:
                #time.sleep(4)
                window1 = pygame.display.set_mode((600,250),0,32)
                window1.fill(white)
                window1.blit(txt7,txt7rect)
                window1.blit(txt9,txt9rect)
                window1.blit(txt9,txt9rect)
                txt3rect.centerx = 300
                txt3rect.centery = 150
                window1.blit(txt3,txt3rect)
                window1.blit(txt10,txt10rect)
                pygame.display.update()
                running3 = False
    if event.type==MOUSEBUTTONDOWN:
        print 'here'
        window = pygame.display.set_mode((width,height+50),0,32)
        board = reversim2.newboard()
        printboard(board)
        i_curplayer=1
        i_depth = 3
        board1= reversim2.hints(board,i_curplayer,-i_curplayer)
        txt5 = font.render('undo',True,black)
        txt5rect = txt5.get_rect()
        txt5rect.centerx = width/2+150
        txt5rect.centery = height+30
        previous = []
        previous.append(board)
        running1 = True
        #running2 = False
  while running1:
    if i_curplayer>0:
      #window.fill(white)
      txt4 = font.render('your turn',True,blue)
      txt4rect = txt4.get_rect()
      txt4rect.centerx = width/2-150
      txt4rect.centery = height+30
      window.blit(txt4,txt4rect)    
      window.blit(txt5,txt5rect)
      pygame.draw.rect(window,black,txt5rect,3)
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        
        if i_curplayer==1:
          for i in range(8):
            for j in range(8):
              if isptinsiderect(event.pos,my[i][j]['rect']):
                k = [i,j]
                previous.append(board)
                if moveuser(k,board,i_curplayer)!=board:
                  
                  board = moveuser(k,board,i_curplayer)
                  board1 = board
                  i_curplayer=-i_curplayer
          if isptinsiderect(event.pos,txt5rect):
                print 'undo'
                if len(previous)!=0:
                  board = previous[-1]
                  board1 = reversim2.hints(board,i_curplayer,-i_curplayer)
                  del(previous[-1])
      if event.type==KEYUP:
        if event.key == K_ESCAPE:
          pygame.quit()
          sys.exit()
    
    pygame.display.update()
    window.fill(white)
    if i_curplayer>0:
      txt4 = font.render('your turn',True,blue)
      txt4rect = txt4.get_rect()
      txt4rect.centerx = width/2-150
      txt4rect.centery = height+30
      window.blit(txt4,txt4rect)
      window.blit(txt5,txt5rect)
      pygame.draw.rect(window,black,txt5rect,3)
    
    for i in range(8):
      for j in range(8):
        pygame.draw.rect(window,my[i][j]['colour'],my[i][j]['rect'])
        pygame.draw.line(window,blue,(0,size*j),(width,size*j))
      pygame.draw.line(window,blue,(i*size,0),(size*i,height))
    pygame.draw.line(window,blue,(0,height),(width,height))
    printboard(board1)
    
    txt1 = 'your score = '+str(reversim2.sumpl(1,board))
    txt2 = 'my score = '+str(reversim2.sumpl(-1,board))
    txt3 = font.render(txt1+' , '+txt2,True,blue)
    txt3rect = txt3.get_rect()
    txt3rect.centerx = width/2-130
    txt3rect.centery = height+10
    window.blit(txt3,txt3rect)
    pygame.display.update()
    #clock.tick(10)
    window.fill(white)
    if i_curplayer>0:
      #window.fill(white)
      txt4 = font.render('your turn',True,blue)
      txt4rect = txt4.get_rect()
      txt4rect.centerx = width/2-150
      txt4rect.centery = height+30
      window.blit(txt4,txt4rect)    
      window.blit(txt5,txt5rect)
      pygame.draw.rect(window,black,txt5rect,3)
    for i in range(8):
      for j in range(8):
        pygame.draw.rect(window,my[i][j]['colour'],my[i][j]['rect'])
        pygame.draw.line(window,blue,(0,size*j),(width,size*j))
      pygame.draw.line(window,blue,(i*size,0),(size*i,height))
    pygame.draw.line(window,blue,(0,height),(width,height))
    printboard(board1)
    if i_curplayer==-1:
      txt4 = font.render('my turn',True,blue)
      txt4rect = txt4.get_rect()
      txt4rect.centerx = width/2-150
      txt4rect.centery = height+30
      window.blit(txt4,txt4rect)
      pygame.display.update()
      board = reversim2.compreturns(i_curplayer,-i_curplayer,board,i_depth)
      i_curplayer =-i_curplayer
      board1 = reversim2.hints(board,i_curplayer,-i_curplayer)
      time.sleep(0.5)
    printboard(board1)
    txt1 = 'your score = '+str(reversim2.sumpl(1,board))
    txt2 = 'my score = '+str(reversim2.sumpl(-1,board))
    txt3 = font.render(txt1+' , '+txt2,True,blue)
    txt3rect = txt3.get_rect()
    txt3rect.centerx = width/2-130
    txt3rect.centery = height+10
    window.blit(txt3,txt3rect)
    if len(reversim2.validlist(i_curplayer,-i_curplayer,board))==0:
      i_curplayer =-i_curplayer
    pygame.display.update()
    if len(reversim2.validlist(i_curplayer,-i_curplayer,board))==0 and len(reversim2.validlist(-i_curplayer,i_curplayer,board))==0:
      time.sleep(2)
      running1 = False
      running2 = True
      txt8 = "press 'a' or click to play again"
      if reversim2.sumpl(1,board)>reversim2.sumpl(-1,board):
        txt6 = "you win"
      if reversim2.sumpl(1,board)<reversim2.sumpl(-1,board):
        txt6 = "i win "
      if reversim2.sumpl(1,board)==reversim2.sumpl(-1,board):
        txt6 = "match draw "
      window1 = pygame.display.set_mode((600,250),0,32)
      window1.fill(white)
      txt7 = font1.render(txt6,True,blue)
      txt7rect = txt7.get_rect()
      txt7rect.centerx = 300
      txt7rect.centery = 50
      window1.blit(txt7,txt7rect)
      txt9 = font1.render(txt8,True,blue)
      txt9rect = txt9.get_rect()
      txt9rect.centerx = 300
      txt9rect.centery = 100
      window1.blit(txt9,txt9rect)
      txt3rect.centerx = 300
      txt3rect.centery = 150
      window1.blit(txt3,txt3rect)
      txt10rect.centerx = 300
      txt10rect.centery = 200
      window1.blit(txt10,txt10rect)
      pygame.display.update()
