#Initiation
import requests
import math
import pygame
from bs4 import BeautifulSoup
URL = 'https://www.puzzle-star-battle.com/?size=8'



#Scrape Web
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = str(soup.find_all(type="text/javascript")[1])
info = soup.find(class_="puzzleInfo")



#Find Board
start=results.index("'")+1
end=results.index("'",start)
board=results[start:end].split(",")
size=int(info.text[:info.text.index("x")])



#Function for drawing lines, couldn't care how messy it is at this point
def drawLine(x,y):
	(xv,xp,yv,yp)=(x*500/size+5,(x+1)*500/size+5,y*500/size+5,(y+1)*500/size+5)
	try:
		pygame.draw.line(screen,(0,0,0),(xv,yv),(xp,yv),(borders[x+y*size].index('t')!=None)*math.floor(60/size))
	except:
		pygame.draw.line(screen,(0,0,0),(xv,yv),(xp,yv),math.floor(20/size))
	try:
		pygame.draw.line(screen,(0,0,0),(xv,yp),(xp,yp),(borders[x+y*size].index('b')!=None)*math.floor(60/size))
	except:
		pygame.draw.line(screen,(0,0,0),(xv,yp),(xp,yp),math.floor(20/size))
	try:
		pygame.draw.line(screen,(0,0,0),(xv,yv),(xv,yp),(borders[x+y*size].index('l')!=None)*math.floor(60/size))
	except:
		pygame.draw.line(screen,(0,0,0),(xv,yv),(xv,yp),math.floor(20/size))
	try:
		pygame.draw.line(screen,(0,0,0),(xp,yv),(xp,yp),(borders[x+y*size].index('r')!=None)*math.floor(60/size))
	except:
		pygame.draw.line(screen,(0,0,0),(xp,yv),(xp,yp),math.floor(20/size))



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
background_colour = (255,255,255)
(width, height) = (512, 512)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(info.text)
running = True


#Run PyGame
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	screen.fill(background_colour)
	for x in range(size):
		for y in range(size):
			drawLine(x,y)
	pygame.display.flip()
