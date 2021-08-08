import os
import time
import math 

class Calculadora:
		
	def Somar(self,n):
		soma = sum(n)
		return print(f"\n	 ◇  Soma  : {soma:.2f}")
		
		
	def Subtrair(self,n1,n2):
		sub = n1 - n2
		return print(f"\n 	◇  Subtração  : {sub:.2f}")
		
		
	def Multiplicar(self,n1,n2):
		multi = n1 * n2
		return print(f"\n 	◇  Multiplicação  : {multi:.2f}")
			
			
	def Dividir(self,n1,n2):
		div = n1 / n2
		return print(f"\n 	◇  Divisão por {n2}  : {div:.2f}")
		
	
	def Média(self, n):
		med = sum(n) / len(n)
		return print(f"\n 	◇  Média : {med:.2f}")
		
	
	def Permutação(self, n1):
		permut = math.factorial(n1)
		return print(f"\n 	◇  Permtação de {n1} é  : {permut:.2f}")
		 
		
	def Porcentagem(self, n1, n2):
		porc = n1 * n2/100
		return print(f"\n 	◇  {n2}% de {n1} é  : {porc:.2f}")
		
		
	def Expoente(self, n1, n2):
		expo= n1 ** n2
		return print(f"\n 	◇  {n1} elevado a {n2} é  : {expo:.2f}")

		
app = Calculadora()
relatorio = {}
tot_relatorio = [ ]
montante = [ ]
clear = 0
while True:
	escolha = " "
	clear += 1
	lista = [1,2,3,4,5,6,7,8,9,0]
	while escolha not in lista:
		print(""" 
				[  Calculadora ]
				
			[ 1 ] - Somar 
			[ 2 ] - Subtrair
			[ 3 ] - Multiplicar
			[ 4 ] - Dividir 
			[ 5 ] - Média 
			[ 6 ] - Permutação
			[ 7 ] - Porcentagem
			[ 8 ] - Potenciação
			[ 9 ] - Sair.""")
		escolha = int(input("\n   • Que opção desejas ? "))
		if escolha == 1:
			print("\n")
			number_1 = float(input(f"  •  Número__01 : "))
			number_2 = float(input(f"  •  Número__02 : "))
			montante.append(number_1)
			montante.append(number_2)
			app.Somar(montante)
			print("\n" * 2, "___" * 12)
		elif escolha == 2:
			print("\n")
			number_1 = float(input(f"  •  Número__01 : "))
			number_2 = float(input(f"  •  Número__02 : "))
			app.Subtrair(number_1,number_2)
			
			print("\n" * 2, "___" * 12)
		elif escolha == 3:
			print("\n")
			number_1 = float(input(f"  •  Número__01 : "))
			number_2 = float(input(f"  •  Número__02 : "))
			app.Multiplicar(number_1,number_2)
			print("\n" * 2, "___" * 12)	
		elif escolha == 4:
			print("\n")
			number_1 = float(input(f"  • Número : "))
			number_2 = float(input(f"  • Divisor : "))
			app.Dividir(number_1,number_2)
			print("\n" * 2, "___" * 12)	
		elif escolha == 5:
			print("\n ")
			tot = int(input("  • Qtd  de termos  : "))
			termo= [ ]
			for y in range(tot):	
				number = float(input(f"  • Número : "))
				termo.append(number)
			app.Média(termo)		
			print("\n" * 2, "___" * 12)
		elif escolha == 6:
			print("\n")
			number_1 = float(input(f"  • Número : "))
			number_2 = 0 
			app.Permutação(number_1)
			print("\n" * 2, "___" * 12)
		elif escolha == 7:
			print("\n")
			number_1 = float(input(f"  • Número Total  : "))
			number_2 = float(input(f"  • Taxa de  % :  : "))
			app.Porcentagem(number_1,number_2)
			print("\n" * 2, "___" * 12)
		elif escolha == 8:
			print("\n")
			number_1 = float(input(f"  • Número   : "))
			number_2 = float(input(f"  • Valor do Expoente:  : "))
			app.Expoente(number_1,number_2)
			print("\n" * 2, "___" * 12)	
	if escolha == 9:
		break
	if clear == 2:
		print("\n Limpando operações antigas...")
		time.sleep(1.2)
		clear = 0
		os.system("clear")
		