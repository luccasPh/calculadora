from math import *

class Log_Cal(object):
	def calcular(self):
		try:
			self.new_conta = format(eval(self.new_conta),".12g")
		except (OverflowError,ZeroDivisionError):
			self.new_conta = "Infinity"
		except:
			self.new_conta = "ERROR"

	def operacao(self):
		self.new_conta = ""
		i = 0
		while i < len(self.conta):

			if self.conta[i] == "!":
				if self.conta[i-1] == "%":
					pad = 0
					pae = 0
					d = ""
					V = True
					for j in range(len(self.new_conta)-1,-1,-1):
						if self.new_conta[j] == ")":
							pad += 1
						elif self.new_conta[j] == "(":
							pae += 1
						elif pad == pae:
							y = j
							break
					for k in range(len(self.new_conta)):
						d += self.new_conta[k]
						if k == y and V:
							d += "gamma("
							V = False
					i += 1
					self.new_conta = d + "+1)"

				elif self.conta[i-1] == ")":
					pad = 0
					pae = 0
					d = ""
					V = True
					for j in range(len(self.new_conta)-1,-1,-1):
						if self.new_conta[j] == ")":
							pad += 1
						elif self.new_conta[j] == "(":
							pae += 1
						elif pad == pae:
							if self.new_conta[j-1] == "o":
								y = j-2
							elif self.new_conta[j-1] == "1":
								y = j-4
							elif self.new_conta[j-1] == "r":
								y = j-3
							else:
								y = j+1
							break
					for k in range(len(self.new_conta)):
						d += self.new_conta[k]
						if k+1 == y and V:
							d += "gamma("
							V = False
					i += 1
					self.new_conta = d + "+1)"
				else:
					r = ""
					v = True
					for z in range(len(self.new_conta)-1,-1,-1):
						if self.new_conta[z] == " " or self.new_conta[z] == "+" or self.new_conta[z] == "-"or self.new_conta[z] == "*" or self.new_conta[z] == "/" or self.new_conta[z] == "(":
							q = z
							break
					for z in range(len(self.new_conta)):
						r += self.new_conta[z]
						if z == q and v:
							r += "gamma("
							v = False 
					i += 1
					self.new_conta = r + "+1)"

			elif self.conta[i] == "l":
				if self.conta[i+1] == "n":
					self.new_conta += "log"
					i += 2
				else:
					self.new_conta += "log10"
					i += 3

			elif self.conta[i] == "√":
				self.new_conta += "sqrt"
				i += 1
					
			elif self.conta[i] == "^":
				self.new_conta += "**"
				i += 1
				
			elif self.conta[i] == "x":
				self.new_conta += "*"
				i += 1

			elif self.conta[i] == "%":
				if self.conta[i-1] == "!":
					d = ""
					V = True
					for j in range(len(self.new_conta)-1,-1,-1):
						if self.new_conta[j] == "a" and self.new_conta[j-1] == "g":
							y = j-1
					for k in range(len(self.new_conta)):
						d += self.new_conta[k]
						if k+1 == y and V:
							d += "("
							V = False
					i += 1
					self.new_conta = d + "/100)"
					
				elif self.conta[i-1] == ")":
					pad = 0
					pae = 0
					d = ""
					V = True
					for j in range(len(self.new_conta)-1,-1,-1):
						if self.new_conta[j] == ")":
							pad += 1
						elif self.new_conta[j] == "(":
							pae += 1
						elif pad == pae:
							if self.new_conta[j-1] == "o":
								y = j-2
							elif self.new_conta[j-1] == "1":
								y = j-4
							elif self.new_conta[j-1] == "r":
								y = j-3
							else:
								y = j+1
							break
					for k in range(len(self.new_conta)):
						d += self.new_conta[k]
						if k+1 == y and V:
							d += "("
							V = False
					i += 1
					self.new_conta = d + "/100)"
				else:
					r = ""
					v = True
					for z in range(len(self.new_conta)-1,-1,-1):
						if self.new_conta[z] == " " or self.new_conta[z] == "+" or self.new_conta[z] == "-"or self.new_conta[z] == "*" or self.new_conta[z] == "/":
							q = z
							break
					for z in range(len(self.new_conta)):
						r += self.new_conta[z]
						if z == q and v:
							r += "("
							v = False 
					i += 1
					self.new_conta = r + "/100)"
			elif self.conta[i] == "÷":
				self.new_conta += "/"
				i += 1
			elif self.conta[i] == "s":
				self.new_conta += "sin"
				i += 3
			elif self.conta[i] == "c":
				self.new_conta += "cos"
				i += 3
			elif self.conta[i] == "s":
				self.new_conta += "sin"
				i += 3
			elif self.conta[i] == "t":
				self.new_conta += "tan"
				i += 3
			elif self.conta[i] == "e":
				if self.conta[i+1] == "x":
					self.new_conta += "exp"
					i += 3
				else:
					self.new_conta += "e"
					i += 1
			elif self.conta[i] == "π":
				self.new_conta += "pi"
				i += 1
			elif self.conta[i] == "r":
				self.new_conta += "radians"
				i += 4
			elif self.conta[i] == "g":
				self.new_conta += "degrees"
				i += 4
			else:
				self.new_conta += self.conta[i]
				i += 1

