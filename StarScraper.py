#Initiation
import requests
from bs4 import BeautifulSoup
symbols=["🟥 ","🟧 ","🟨 ","🟩 ","🟦 ","🟪 ","🟫 ","⬛ ","⬜ ","🧱 "]
URL='https://www.puzzle-star-battle.com/?size=5'

#Scrape Web
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = str(soup.find_all(type="text/javascript")[1])
info = soup.find(class_="puzzleInfo")

#Find Board
start=results.index("'")+1
end=results.index("'",start)
board=results[start:end].split(",")

#Board Output
for y in range(10):
	row=""
	for x in range(10):
		row=row+symbols[int(board[x+y*10])-1]
	print(row)
print(info.text)
