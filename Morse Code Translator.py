Dictionary = {"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--",
              "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":".--.", "Y":"-.--", "Z":"--..",
              "0":"-----", "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"----.",
              "&":".-...", "'":".----.", "@":".--.-.", ")":"-.--.-", "(":"-.--.", ":":"---...", ",":"--..--", "=":"-...-",
              "!":"-.-.--", "+":".-.-.", "\"":".-..-.", "?":"..--..", "/":"-..-.", ".":".-.-.-", "-":"-....-", " ":"/"}

def encrypt(message):
	cipher = ''
	for letter in message:
		if Dictionary.get(letter.upper()) != None:
			cipher += Dictionary[letter.upper()] + ' '
		else:
			raise SystemExit("Error encrypting")
	return cipher

def decrypt(message):
	message += ' '
	decipher = ''
	citext = ''
	for letter in message:
		if Dictionary.get(letter) != None:
			if (letter != ' '):
				i = 0
				citext += letter
			else:
				i += 1
				if i == 2 :
					decipher += ' '
				else:
					decipher += list(Dictionary.keys())[list(Dictionary
					.values()).index(citext)]
					citext = ''
		else:
			raise SystemExit("Error decrypting")
	return decipher
# Enter your message here
message = "Hello"
result = encrypt(message.upper())
print (result)
message = ".... . .-.. .-.. ---"
result = decrypt(message)
print (result)
