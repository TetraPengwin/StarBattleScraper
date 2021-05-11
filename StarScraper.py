#Initiation
import requests
import math
import pygame
from bs4 import BeautifulSoup
URL = 'https://www.puzzle-star-battle.com/?size=9'



#Scrape Web
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = str(soup.find_all(type="text/javascript")[1])
info = soup.find(class_="puzzleInfo")
if info.text[1]=="★":
	puzzle = info.text[:info.text.index("  ")+1]
	info = soup.find("option")
	puzzle = puzzle+info.text
else:
	puzzle=info.text



#Find Board
start=results.index("'")+1
end=results.index("'",start)
board=results[start:end].split(",")
size=int(math.sqrt(len(board)))



#Function for drawing lines, couldn't care how messy it is at this point
def drawLine(x,y):
	(xv,xp,yv,yp)=(x*500/size+5,(x+1)*500/size+5,y*500/size+5,(y+1)*500/size+5)
	try:
		pygame.draw.line(screen,(0,0,0),(xv,yv),(xp,yv),(borders[x+y*size].index('t')!=None)*6)
	except:
		pygame.draw.line(screen,(0,0,0),(xv,yv),(xp,yv),1)
	try:
		pygame.draw.line(screen,(0,0,0),(xv,yp),(xp,yp),(borders[x+y*size].index('b')!=None)*6)
	except:
		pygame.draw.line(screen,(0,0,0),(xv,yp),(xp,yp),1)
	try:
		pygame.draw.line(screen,(0,0,0),(xv,yv),(xv,yp),(borders[x+y*size].index('l')!=None)*6)
	except:
		pygame.draw.line(screen,(0,0,0),(xv,yv),(xv,yp),1)
	try:
		pygame.draw.line(screen,(0,0,0),(xp,yv),(xp,yp),(borders[x+y*size].index('r')!=None)*6)
	except:
		pygame.draw.line(screen,(0,0,0),(xp,yv),(xp,yp),1)



#Set Draw State Of Grid
borders=[]
for i in range(size*size): borders.append("")
for y in range(size):
	for x in range(size):
		if y==0 or board[x+y*size-size]!=board[x+y*size]: borders[x+y*size]=borders[x+y*size]+"t"
		if y==size-1 or board[x+y*size+size]!=board[x+y*size]: borders[x+y*size]=borders[x+y*size]+"b"
		if x==0 or board[x+y*size-1]!=board[x+y*size]: borders[x+y*size]=borders[x+y*size]+"l"
		if x==size-1 or board[x+y*size+1]!=board[x+y*size]: borders[x+y*size]=borders[x+y*size]+"r"



#Create PyGame Window
screen = pygame.display.set_mode((512, 512))
pygame.display.set_caption(puzzle)
running = True


#Run PyGame
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	screen.fill((255,255,255))
	for x in range(size):
		for y in range(size):
			drawLine(x,y)
	pygame.display.flip()
