

# NOTE: this example requires PyAudio because it uses the Microphone class
import keyboard
import time
import pyttsx3
import speech_recognition as sr
import Echo_voice
import webbrowser
import sys
import _thread
import os

firefox_path="C:\Program Files\Mozilla Firefox\firefox.exe"
#webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path),1)
def voice(line):
	echo = Echo_voice.voice()
	echo.start(line)
	del(echo)
hibernating = False
def command_parsing(command):
	string = command.lower()
	print(string)
	if string.split()[0]=="echo":
		list = string.split()
		str = ""
		for word in list[1:]:
			str += word + " "
			
		string = str
		print(string)
		
		if 'open firefox' in string:
			voice("Opening...")
			webbrowser.get("open -a C:\\Program F~\\Mozilla Firefox\\firefox.exe %s")
			webbrowser.open('http://google.com')
		elif 'close program' in string:
			stop_listening(wait_for_stop=False)
			voice("See you!")
			os._exit(0)
		elif 'go to sleep' in string:
			voice("Good night...")
			os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
			
			os._exit(0)
		elif 'say' or 'say this' in string:
			voice(string[3:])	
		else:
			voice("I did not understand you")
		
	
	
	

# this is called from the background thread
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
	try:
		quiery = recognizer.recognize_google(audio)
		print(quiery)
		command_parsing(quiery)

		# echo = Echo_voice.voice()
		# echo.start("You said: " + quiery)
		# del(echo)
	except sr.UnknownValueError:
		#print("Skip line")
		pass
	except sr.RequestError as e:
		pass
		#print("Sphinx error; {0}".format(e))


r = sr.Recognizer()
m = sr.Microphone()


with m as source:
	r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)
# `stop_listening` is now a function that, when called, stops background listening

# calling this function requests that the background listener stop listening
while True:
	try:
		if keyboard.is_pressed('a'): 
			stop_listening(wait_for_stop=False)
			break
		
		pass


	except:
		pass
