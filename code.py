from socket import *
from threading import Thread

# class Player(Thread): 
 
#     def __init__(self,ip,port): 
#         Thread.__init__(self) 
#         self.ip = ip 
#         self.port = port 
#         print "[+] New server socket thread started for " + ip + ":" + str(port) 
 
#     def run(self): 
#         while True : 
#             data = clientSocket.recv(2048)
#             if data=='exit':
#                 clientSocket.close()
#             MESSAGE = raw_input("Multithreaded Python server :")
#             if MESSAGE == 'exit':
#                 clientSocket.close()
#                 break
#             clientSocket.send(MESSAGE)  # echo 
 
# tcpServer = socket(AF_INET, SOCK_STREAM)
# tcpServer.bind(('', 5000)) 
# threads = [] 
 
# while True: 
#     tcpServer.listen(4) 
#     clientSocket,clientAddress = tcpServer.accept()
#     newthread = Player(clientAddress[0],clientAddress[1]) 
#     newthread.start() 
#     threads.append(newthread) 
 
# for t in threads: 
#     t.join() 

# tcpServer.close()

# from socket import *
# from threading import Thread

# class Player(Thread):
#     def __init__(self,ip,port,num):
#         Thread.__init__(self)
#         self.ip = ip
#         self.port = port
#         self.msg = ""
#         self.num = num
#         self.talk = clientSocket

#     def run(self):
#         while self.msg != "exit":
#             self.msg = self.talk.recv(2048).strip()
#             self.talk.send("OK\n")
#             print "msg",self.msg,self.num
#         self.talk.close()
#         # print self.ip,self.port
    
#     def address(self):
#         return self.ip

# threadPool = []
# counter = 0

# tcpServer = socket(AF_INET,SOCK_STREAM)
# tcpServer.bind(('',5000))
# tcpServer.listen(5)
# # tcpServer.setblocking(False)

# while counter<2:
#     clientSocket,clientAddress = tcpServer.accept()
#     newThread = Player(clientAddress[0],clientAddress[1],counter+1)
#     newThread.start()
#     threadPool.append(newThread)
#     counter += 1

# for t in threadPool:
#     t.join()