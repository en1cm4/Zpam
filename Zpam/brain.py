from pynput.keyboard import Key, Controller
import time
import os
os.system("cls")

teclear = Controller()
print(r"""
  ______                      
 |___  /                      
    / / _ __   __ _ _ __ ___  
   / / | '_ \ / _` | '_ ` _ \ 
  / /__| |_) | (_| | | | | | |
 /_____| .__/ \__,_|_| |_| |_|
       | |                    
       |_| 
           		 	         ___        __ 
				        / _ \      /_ |
				 __   __ | | |      | |
				 \ \ / / | | |      | |
				  \ V /| |_| |  _   | |
				   \_/  \___/  (_)  |_|
				                       
                
	""")


print("""

Eliga una opcion...
1) Texto
2) Numeros
3) Contar hasta...
4) Salir

	""")



def zpam(send, texto, sec):
	
	while contador < send:
		teclear.type(texto)
		teclear.press(Key.enter)
		time.sleep(sec)
		contador += 1


opc = int(input())

if opc ==1:
	print("Ingrese el texto que desea repetir...")
	texto = input()


	print("¿Cuantas veces enviaremos este mensaje...?")
	send = int(input())

	print("¿Cada cuanto tiempo... ? Ingresar en segundos...")
	sec = int(input())

	print("Tienes 5 segundos para ir a la ventana")
	time.sleep(5)

	contador = 0

	while contador < send:
		teclear.type(texto)
		teclear.press(Key.enter)
		time.sleep(sec)
		contador += 1

elif opc ==2:

	print("Que numero desea repetir...")
	texto = input()


	print("¿Cuantas veces enviaremos este mensaje...?")
	send = int(input())

	print("¿Cada cuanto tiempo... ? Ingresar en segundos...")
	sec = int(input())

	print("Tienes 5 segundos para ir a la ventana")
	time.sleep(5)

	contador = 0

	while contador < send:
		teclear.type(texto)
		teclear.press(Key.enter)
		time.sleep(sec)
		contador += 1



elif opc ==3:

	print("Hasta que numero contaremos...")
	send = int(input())

	print("¿Cada cuanto tiempo... ? Ingresar en segundos...")
	sec = int(input())

	print("Tienes 5 segundos para ir a la ventana")
	time.sleep(5)

	contador = 0

	while contador < send:

		time.sleep(sec)

		contador += 1
		teclear.type(str(contador))
		teclear.press(Key.enter)

elif opc ==4:
	print("Okei, ten buen dia!!")
	time.seep(2)
	exit()

else:
	print("Comando desconocido, ten buen dia")
	time.sleep(1.5)

	