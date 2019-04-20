#
#
#
import mfrc522
from os import uname

def read():

	#Provoca rst usando 0,2
	#possivelmente precisa esperar um tempo para poder usar estes pinos
	#pois fazem parte o boot
	#rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)
	rdr = mfrc522.MFRC522(12, 13, 4, 5, 14)
	
	while (True):
		
		print("")
		print("Place card before reader to read from address 0x08")
		print("")

		try:
			(stat, tag_type) = rdr.request(rdr.REQIDL)
		
			if stat == rdr.OK:
				(stat, raw_uid) = rdr.anticoll()
				if stat == rdr.OK:
					return (tag_type, raw_uid)
				#else:
				#	return (False, 0, 0)
			#else:
			#	return (False, 0, 0)
					
		except KeyboardInterrupt:
			print("Bye")
			#return (False, 0, 0)
#####################################################################
