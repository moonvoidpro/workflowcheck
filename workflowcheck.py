# -*- coding:utf-8 -*-
#implemented in py3
import win32gui
import time
import winsound
import win32api
import easygui

def remindtocode():

	frequency = 2500
	duration = 1000
	winsound.Beep(frequency, duration)
	#print('Beep')
	print('起床写代码啦!!~~~~')
	alert = easygui.buttonbox(msg = '起床写代码啦!!~~~~', title = 'workflowcheck', choices = ['Yes'])
	
notdoingwork = 0
nottouchingPC = 0
needremind = False
lastinputtime = 0


#for i in range(1,4):
toolname = input('tool of dev:')


while(1):
	
	time.sleep(60)
	
	if(lastinputtime == win32api.GetLastInputInfo()):
		print('别摸鱼啦~')
		nottouchingPC += 1
		if(nottouchingPC > 5):
			needremind = True
	else:
		nottouchingPC = 0
		
	lastinputtime = win32api.GetLastInputInfo()
	
	hwnd = win32gui.GetForegroundWindow()
	title_text = win32gui.GetWindowText(hwnd)
	#title_text = title_text.decode('gbk').encode('utf-8') 
	#print(title_text)
	if toolname not in title_text:
		print('还不搬砖？')
		notdoingwork += 1
		if(notdoingwork >5):
			needremind = True		
	else:
		notdoingwork = 0
		
	if(needremind):
		remindtocode()
		needremind = False

	
 
