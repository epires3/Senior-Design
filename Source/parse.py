##########################################
# Transmission Data Parsing Routine	 							
# Created by: Eric Pires									
# April 2nd 2018										
# COMET Senior Design Project									
# University of Massachusetts Dartmouth								
##########################################

import os
head = "\x89PNG"
foot = "\x00IEND\xaeB`\x82"

# Prints to terminal upon completion of data transmission 
def success():
	print("\n--------------------------------------------")
	print("Transmission Received")
	print("--------------------------------------------\n")

# Locates preamble in raw USRP output dump
def get_preamble(data):
	start = data.find(head)
    	end = data.find(foot,start)
	return start,end

# Returns True when packet is incomplete, False when packet is completed
def checksum(start,end,data):
	if(start != -1) and (end != -1):
		success()
	    	out = open('out.png','wb')
		out.write(data[start:end+9])
		out.close()
		# Terminates GUI on preamble match instead of having to manually exit the GUI
		os.system("kill $(ps -h | grep '[p]ython' | awk '{print $1}')")
		return False
	return True
# Main polling function that completes upon successful data reception
def main():
	rx = True
	while rx :
		file = open('RX.png','rb')
		recv = file.read()
	    	start,end = get_preamble(recv)
		rx = checksum(start,end,recv)
	file.close()

main()
	    	
