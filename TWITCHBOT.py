import socket
import pyautogui

SERVER = "irc.twitch.tv"
PORT = 6667
PASS = "oauth:jqjn5g5eop3ppx2y2yu2py4parc40v"
BOT = "Twitchbotmidi"
CHANNEL = "justinwabs"
OWNER = "justinwabs"
irc = socket.socket()
irc.connect((SERVER, PORT))
irc.send(("PASS " + PASS + "\n" +
	      "NICK " + BOT + "\n" +
	      "JOIN #" + CHANNEL + "\n").encode())

def gamecontrol():
	while True:
		if "c" in message.lower():
			pyautogui.keydown('q')
			message = ""
			pyautogui.keyup('q')


def joinchat():
	Loading = True
	while Loading:
		readbuffer_join = irc.recv(1024)
		readbuffer_join = readbuffer_join.decode()
		for line in readbuffer_join.split("\n")[0:-1]:
			print(line)
			Loading = loadingcomplete(line)
def loadingcomplete(line):
	if ("End of /NAMES list" in line):
		print("Bot has joined " + CHANNEL + "'s Channel!")
		sendMessage(irc, "joined room")
		return False
	else:
		return True
def sendMessage(irc, message):
	messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
	irc.send((messageTemp + "\n").encode())
def getUser(line):
	seprate = line.split(":", 2)
	user = seprate[1].split("!" , 1)[0]
	print(user)
	return user
def getMessage(line):
	try:
		messa
		ge = (line.split(":",2))[2]
	except:
		message = ""
	return message
def console(line):
	if "PRIVMSG" in line:
		return False
	else:
		return True

joinchat()



echo "# twitchbottest" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/justinwabs/twitchbottest.git
git push -u origin master


