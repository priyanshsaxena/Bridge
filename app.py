from Tkinter import *          
import random
from socket import *
from threading import Thread
import time

purpose = None
nameCollect = None
tBox = None
board = None

cardImages = []

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

class Round():

	bids = []
	contract = ""
	contractMaker = -1
	dealer = -1

	def __init__(self):
		bids = [[],[],[],[]]
		contract = ""
		contractMaker = -1
		dealer = -1
		# pass

	def __str__(self):
		return str(self.contractMaker) + " with " + contract
		# pass

def countLongSuit(hand):
	s,h,d,c = [i for i in hand if i in range(39,52)],[i for i in hand if i in range(26,39)],[i for i in hand if i in range(13,26)],[i for i in hand if i in range(13)]
	return max(len(s)-4,0)+max(len(h)-4,0)+max(len(d)-4,0)+max(len(c)-4,0)

def countHCP(hand):
	return sum(map(lambda x:(x%13)-8,filter(lambda x: (x%13)>8,hand)))

# how to make computer-bid ?
def computerBid():
	return "pass"

# changes size of a frame on card-play
def discard(someFrame):
	print called
	someFrame.configure(width=(someFrame.winfo_width()*1.0/13))
	# self.destroy()
	print "name"

def OK():
	global nameCollect
	global purpose
	global tBox
	global cardImages
	print tBox.get()
	nameCollect.destroy()
	board = Tk()
	board.configure(background='green')
	board.minsize(800,600)
	board.title("Bridge - Play!")
	lateralFrames = Frame(board,bg='green',width=800,height=400,bd=2)
	frameNorth = Frame(board,bg='white',highlightbackground='red',highlightthickness=1,width=390,height=43.65,bd=2)
	frameSouth = Frame(board,bg='white',highlightbackground='red',highlightthickness=1,width=390,height=43.65,bd=2)
	frameEast = Frame(lateralFrames,bg='white',highlightbackground='red',highlightthickness=1,width=43.65,height=390,bd=2)
	frameWest = Frame(lateralFrames,bg='white',highlightbackground='red',highlightthickness=1,width=43.65,height=390,bd=2)
	endButton = Button(lateralFrames, text="Play!",command= lambda: discard(frameSouth))
	clubCards = []
	for i in range(13):
		b = Button(frameSouth)
		b.image = cardImages[i]
		clubCards.append(b)
	frameNorth.pack()
	frameEast.pack(side=LEFT,padx=(0,200))
	endButton.pack(side=LEFT, padx=50,pady=200)
	frameWest.pack(side=RIGHT,padx=(200,0))
	lateralFrames.pack()
	for i in range(13):
		clubCards[i]['command'] = lambda: discard(clubCards[i])#clubCards[i].pack_forget()
		clubCards[i].pack(side=LEFT)
	frameSouth.pack()
	board.mainloop()

def main():
	global cardImages
	global nameCollect
	global tBox
	nameCollect = Tk()
	for i in range(52):
		filename = "images/png/"+str(i)+".png"
		cardImages.append(PhotoImage(file=filename))
	purpose = Label(nameCollect,text="Enter your name!")
	purpose.pack()
	tBox = Entry(nameCollect)
	tBox.pack()
	closeButton = Button(nameCollect,text="OK",command=OK)
	closeButton.pack()
	nameCollect.title("Bridge - Enter Your Name")
	nameCollect.mainloop()
	# hand = [1,5,9,43,21,13,26,32,33,45,51,12,14]
	'''threadPool = []
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

	for t in threadPool:
		t.join()

	serverSocket.close()'''

main()