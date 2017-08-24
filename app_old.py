from Tkinter import *           #This interface allow us to draw windows
import random
from socket import *
from threading import Thread
import time

purpose = None
nameCollect = None
tBox = None
board = None

scores = [0,0]
bidRanges = {}
suitValues = { "C" : 6, "D" : 7, "H" : 8, "S" : 9, "NT" : 10 }

class Deck():

	deck = range(52)

	def __init__(self):
		pass

	def shuffle(self):
		pack = deck
		random.shuffle(pack)
		return pack

class Player(Thread):

	defaultOrder = "NESW"
 
	def __init__(self,clientSocket,playerNumber): 
		Thread.__init__(self)
		self.position = "NESW"[playerNumber]
		self.message = ""
		self.playerSocket = clientSocket
		self.hand = []
		self.name = ""
		self.team = playerNumber % 2

	def __str__(self):
		return self.position
 
	def run(self): 
		while self.message != "exit" : 
			self.message = self.playerSocket.recv(2048).strip()
            # logic
			self.playerSocket.send("OK\n")
		self.playerSocket.send("Good game!\n")
		self.playerSocket.close()

	def setHand(self,hand):
		self.hand = hand

	def dealCards(self,players):
		firstCard = self.playerNumber + 1
		order = defaultOrder[firstCard:] + defaultOrder[:firstCard] 
		deck = Deck()
		deck = deck.shuffle()
		for i in range(4):
			players[(firstCard+i)%4].setHand(deck[i*13:(i+1)*13])

def countLongSuit(hand):
	s,h,d,c = [i for i in hand if i in range(39,52)],[i for i in hand if i in range(26,39)],[i for i in hand if i in range(13,26)],[i for i in hand if i in range(13)]
	return max(len(s)-4,0)+max(len(h)-4,0)+max(len(d)-4,0)+max(len(c)-4,0)

def countHCP(hand):
	return sum(map(lambda x:(x%13)-8,filter(lambda x: (x%13)>8,hand)))

def computerBid():
	return "pass"

def OK():
	global nameCollect
	global purpose
	global tBox
	print tBox.get()
	nameCollect.destroy()
	board = Tk()
	board.configure(background='green')
	board.minsize(800,600)
	board.title("Bridge - Play!")
	lateralFrames = Frame(board,bg='green',width=800,height=400,bd=2)
	frameNorth = Frame(board,bg='green',highlightbackground='red',highlightthickness=1,width=400,height=100,bd=2)
	frameSouth = Frame(board,bg='green',highlightbackground='red',highlightthickness=1,width=400,height=100,bd=2)
	frameEast = Frame(lateralFrames,bg='green',highlightbackground='red',highlightthickness=1,width=100,height=400,bd=2)
	frameWest = Frame(lateralFrames,bg='green',highlightbackground='red',highlightthickness=1,width=100,height=400,bd=2)
	frameNorth.pack()
	frameEast.pack(side=LEFT,padx=(0,250))
	frameWest.pack(side=RIGHT,padx=(250,0))
	# frameWest.grid(column=2)
	lateralFrames.pack()
	frameSouth.pack()
	board.mainloop()

def main():
	# global nameCollect
	# global tBox
	# nameCollect = Tk()
	# purpose = Label(nameCollect,text="Enter your name!")
	# purpose.pack()
	# tBox = Entry(nameCollect)
	# tBox.pack()
	# closeButton = Button(nameCollect,text="OK",command=OK)
	# closeButton.pack()
	# nameCollect.title("Bridge - Enter Your Name")
	# nameCollect.mainloop()
	# hand = [1,5,9,43,21,13,26,32,33,45,51,12,14]
	threadPool = []
	players = 0

	serverSocket = socket(AF_INET,SOCK_STREAM)
	serverSocket.bind(('',5000))
	serverSocket.listen(5)

	while players<2:
		clientSocket,clientAddress = serverSocket.accept()
		newThread = Player(clientSocket,players)
		print newThread
		newThread.start()
		threadPool.append(newThread)
		players += 1

	# time.sleep(10)

	for t in threadPool:
		t.join()

	serverSocket.close()

main()