import os
def message(title, message):
	os.system('notify-send "'+title+'" "'+message+'"')
message('mess','first')
