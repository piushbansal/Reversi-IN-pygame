import sys ,time,random
from sys import maxsize
def newboard():
    board = ()
    l = list(board)
    for i in range(8):
        l.append([' ']*8)
    l[3][3]=l[4][4]=1
    l[4][3]=l[3][4]=-1
    for i in range(8):
        l[i]  = tuple(l[i])
    board = tuple(l)
    return board
def getboard(board1):
    return board1
def reset(board):
        print '    1   2   3   4   5   6   7   8 '
        hline = '  *---*---*---*---*---*---*---*---*'
        print hline
        for i in range(8):
            print i+1,
            for j in range(8):
                print '| '+ str(board[i][j]),
            print'|'
            print hline

def hints(board1,ti,oti):
    board = getboard(board1)
    list1 = validlist(ti,oti,board1)
    board1 = list(board)
    for i in range(8):
         board1[i]=list(board[i])
    for x,y in list1:
         board1[x][y]='.'
    for i in range(8):
        board1[i] = tuple(board1[i])
    board1 = tuple(board1)
    return board1

def isonboard(x,y):
  if ((x<8) and (x>=0)) and ((y<8)and (y>=0)):
    return True
  else :
    return False
def isvalid(xs,ys,tile,othertile,board1):
  board = list(board1)
  for i in range(8):
      board[i]=list(board[i])
  if board[xs][ys]!=' ' or not isonboard(xs,ys):
    #print 'here1'
    return False
  else:
    list1 = []
    for xd,yd in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
      x = xs+xd
      y = ys+yd
      if not isonboard(x,y):
        
        continue
      while board[x][y]==othertile:
        x = x+xd
        y = y+yd
        if not isonboard(x,y):
          break
      if not isonboard(x,y):
        continue
      if board[x][y] == tile:
        x = x-xd
        y = y-yd
        while x!=xs or y!=ys:
          list1.append((x,y))
          x = x-xd
          y = y-yd
        continue
    if len(list1)==0:
      
      return False
    else:
      list1 = tuple(list1)
      return list1
def validlist(tile,othertile,board1):
  board = list(board1)
  for i in range(8):
      board[i]=list(board[i])
  
  list1 = []
  for i in range(8):
    for j in range(8):
      if isvalid(i,j,tile,othertile,board):
        list1.append((i,j))
  list1 = tuple(list1)
  return list1

def sumpl(t,board):
  sum1 = 0
  for i in range(8):
    for j in range(8):
      if board[i][j]==t:
        sum1 = sum1+1
  return sum1

def changes(board,ti,oti,x,y):
  board1 = list(board)
  for i in range(8):
     board1[i]=list(board[i])
  if len(validlist(ti,oti,board))==0:
    return board
  list1 = isvalid(x,y,ti,oti,board)
  board1[x][y] = ti
  for i,j in list1:
    board1[i][j] = ti
  for i in range(8):
        board1[i] = tuple(board1[i])
  board1 = tuple(board1)
  return board1
def evalcorners(board,t):
    for i in validlist(t,-t,board):
        if i in cornerposn():
            return 1000*t
    return 0
def iswinning(board,ti,oti):
  if len(validlist(oti,ti,board))==0 and (len(validlist(ti,oti,board))==0):
    if sumpl(ti,board)>sumpl(oti,board):
      return 1
    return 0
  else:
    return 0
class hiBoard:
  def __init__(self,i_depth,i_playernum,board,i_value=0):
    self.children = []
    self.depth = i_depth
    self.playernum = i_playernum
    self.board = board
    self.list = validlist(self.playernum,-self.playernum,board)
    #self.value= i_value
    """
    self.createchildren()
  def createchildren(self):
    if self.depth>=0:
      for i in self.list:
        v = changes(self.board,self.playernum,-self.playernum,i[0],i[1])
        self.children.append(hiBoard(self.depth-1,-self.playernum,v,self.realvalue(v)))
  def realvalue(self,board):
    if iswinning(board,self.playernum,-self.playernum):
      return maxsize*self.playernum+(self.depth)*self.playernum
    if iswinning(board,-self.playernum,self.playernum):
      return maxsize*-self.playernum+(self.depth)*-self.playernum
    #if evalcorners(board,self.playernum
    return 3-(self.depth)*self.playernum

def minimax(board1,i_depth,i_playernum):
  if i_depth==0 or abs(board1.value)>=maxsize/2:
    return board1.value
  i_bestvalue = 2*maxsize*-i_playernum
  if validlist(i_playernum,-i_playernum,board1.board)==[]:
      print 'here is a bug'
  rough = board1.children
  list1 = []
  
  for child in rough:
    #print child.board
    i_value = minimax(child,i_depth-1,-i_playernum)
    list1.append(i_value)
  print list1
  if i_playernum>0:
    return max(list1)
  else:
    return min(list1)
    """
def moveuser(user,board,i_playernum):
  #global usermode
  print validlist(i_playernum,-i_playernum,board)
  if (int(user[1])-1,int(user[0])-1) in validlist(i_playernum,-i_playernum,board):
    print 'here2'
    return changes(board,i_playernum,-i_playernum,int(user[1])-1,int(user[0])-1)
  else:
    user = raw_input("your next move ")
    return moveuser(user,board,i_playernum)
def undo(board,s):
    return board
def removal(previous):
    k = len(previous)
    previous = list(previous)
    del(previous[k-1])
    previous = tuple(previous)
    return previous
def cornerposn():
  return ((0,0),(0,7),(7,7),(7,0))

def intelligence(t,ot,board):
  
  for i in range(4):
    if cornerposn()[i] in validlist(t,ot,board):
      return cornerposn()[i]
  copy = getboard(board)
  list1 = validlist(t,ot,copy)
  list2 = []
  summin = -1
  for k in list1:
    copy = getboard(board)
    #print k
    board2 = changes(copy,t,ot,k[0],k[1])
    if sumpl(t,board2)>=summin:
      summin = sumpl(t,board2)
  for k in list1:
    copy = getboard(board)
    #print k
    board2 = changes(copy,t,ot,int(k[0]),int(k[1]))
    if sumpl(t,board2)==summin:
      p = k
      list2.append(p)
  q = random.choice(list2)
  return q
"""
def compreturns1(t,ot,board,i_depth):
    board1 = hiBoard(i_depth,t,board)
    i_bestvalue = 2*maxsize
    list2 = []
    list3 = []
    for i in range(len(board1.children)):
        t = minimax(board1.children[i],i_depth,ot)
        list2.append(t)
    i_bestvalue = min(list2)
    for i in range(len(list2)):
        if list2[i]==i_bestvalue:
          list3.append(i)
    i_value = random.choice(list3)
    board = board1.children[i_value].board
    return board
"""
def compreturns(t,ot,board,i_depth):
    board1 = hiBoard(i_depth,t,board)
    print len(validlist(t,ot,board))
    if len(validlist(t,ot,board))==0:
        return board
    q = intelligence(t,ot,board)
    board = changes(board,t,ot,q[0],q[1])
    return board
    """
if __name__ == "__main__":
  i_curplayer = 1
  board = newboard()
  reset(board)
  i_depth = 1
  while len(validlist(i_curplayer,-i_curplayer,board))!=0 or len(validlist(-i_curplayer,i_curplayer,board))!=0:
    user = raw_input('give your input')
    print user*2
    print board
    board = moveuser(user,board,i_curplayer)
    reset(board)
    if not iswinning(board,i_curplayer,-i_curplayer):
      print ' i am playing'
      i_curplayer= -i_curplayer
      board1 = hiBoard(i_depth,i_curplayer,board)
      i_bestvalue = 2*maxsize
      list2 = []
      list3 = []
      for i in range(len(board1.children)):
        t = minimax(board1.children[i],i_depth,-i_curplayer)
        print t
        list2.append(t)
      i_bestvalue = min(list2)
      for i in range(len(list2)):
        if list2[i]==i_bestvalue:
          list3.append(i)
      i_value = random.choice(list3)
      board = board1.children[i_value].board
      reset(board)
      i_curplayer= -i_curplayer
      """
