#!/usr/bin/python

import os
import time
import sys
import Quartz
import subprocess

def get_idle_time():
	idle_check = os.popen("echo $((`ioreg -c IOHIDSystem | sed -e '/HIDIdleTime/ !{ d' -e 't' -e '}' -e 's/.* = //g' -e 'q'` / 1000000000))")
	idle_time = idle_check.read().replace('\n', '')
	return idle_time

def lock_after_idle_time_limit(idle_time):
	idle_time_limit = "600"
	d=Quartz.CGSessionCopyCurrentDictionary() # checks if screen is locked already - dont need to lock a locked screen
	print(idle_time, idle_time_limit, idle_time >= idle_time_limit)
	if idle_time >= idle_time_limit and not d.get("CGSSessionScreenIsLocked", 0):
		try:
			subprocess.call("""osascript<<END
				tell application "System Events"
					set textToType to "text here"
					key code 12 using {command down, control down}
				end tell
				END""", shell=True)
		except Exception as e:
			print(e)

def lock_loop():
	while True:	
		lock_after_idle_time_limit(get_idle_time())
		time.sleep(1)

if __name__ == "__main__":
	args = sys.argv
	if '-l' in args:
		lock_loop()
	else:
		lock_after_idle_time_limit(get_idle_time())