#Initiation
import requests
import pygame
from bs4 import BeautifulSoup
URL = 'https://www.puzzle-star-battle.com/?size=5'



#Scrape Web
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = str(soup.find_all(type="text/javascript")[1])
info = soup.find(class_="puzzleInfo")



#Find Board
start=results.index("'")+1
end=results.index("'",start)
board=results[start:end].split(",")



#Function for drawing lines, couldn't care how messy it is at this point
def drawLine(x,y):
	try:
		pygame.draw.line(screen,(0,0,0),(x*50+5,y*50+5),(x*50+55,y*50+5),(borders[x+y*10].index('t')!=None)*6)
	except:
		pygame.draw.line(screen,(0,0,0),(x*50+5,y*50+5),(x*50+55,y*50+5),2)
	try:
		pygame.draw.line(screen,(0,0,0),(x*50+5,y*50+55),(x*50+55,y*50+55),(borders[x+y*10].index('b')!=None)*6)
	except:
		pygame.draw.line(screen,(0,0,0),(x*50+5,y*50+55),(x*50+55,y*50+55),2)
	try:
		pygame.draw.line(screen,(0,0,0),(x*50+5,y*50+5),(x*50+5,y*50+55),(borders[x+y*10].index('l')!=None)*6)
	except:
		pygame.draw.line(screen,(0,0,0),(x*50+5,y*50+5),(x*50+5,y*50+55),2)
	try:
		pygame.draw.line(screen,(0,0,0),(x*50+55,y*50+5),(x*50+55,y*50+55),(borders[x+y*10].index('r')!=None)*6)
	except:
		pygame.draw.line(screen,(0,0,0),(x*50+55,y*50+5),(x*50+55,y*50+55),2)



#Set Draw State Of Grid
borders=[]
for i in range(100): borders.append("")
for y in range(10):
	for x in range(10):
		if y==0 or board[x+y*10-10]!=board[x+y*10]: borders[x+y*10]=borders[x+y*10]+"t"
		if y==9 or board[x+y*10+10]!=board[x+y*10]: borders[x+y*10]=borders[x+y*10]+"b"
		if x==0 or board[x+y*10-1]!=board[x+y*10]: borders[x+y*10]=borders[x+y*10]+"l"
		if x==9 or board[x+y*10+1]!=board[x+y*10]: borders[x+y*10]=borders[x+y*10]+"r"



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
	for x in range(10):
		for y in range(10):
			drawLine(x,y)
	pygame.display.flip()
