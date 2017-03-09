class Caesar():
	
	def __init__(self):
		self.key = None
		
	def setKey(self, key):
		try:
			#If key is an int
			self.key = int(key)
			return True
		except:
			try:
				#If key is a character
				self.key = ord(key.lower())-97
				if self.key < 0 or self.key > 25:
					raise
				return True
			except:
				print("\nError: Key must be an integer or a single character a-z or A-Z")
		
		return False
		
	def encrypt(self, plainText):				
		return self.crypt(plainText, True)
		
	def decrypt(self, cipherText):
		return self.crypt(cipherText, False)
		
	def crypt(self, text, isEncrypt):
		newText = ""
		if isEncrypt:
			mult = 1
		else:
			mult = -1
		for char in text:
			if char.isalpha():
				s = ord('a' if char.islower() else 'A')
				c = chr((ord(char) - s + mult * self.key) % 26 + s)
				newText += c
			else:
				newText += char
		
		return newText
