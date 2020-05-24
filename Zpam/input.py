import os
import time
print(r"""
  ____  _                           _     _       _ 
 |  _ \(_)                         (_)   | |     | |
 | |_) |_  ___ _ ____   _____ _ __  _  __| | ___ | |
 |  _ <| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \| |
 | |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) |_|
 |____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/(_)
                                                    

 						Este es un script de spam

     Para correr el script primero debemos instalar
     una libreria(pynput)! No te preocupes tu decides si lo hacemos.


	""")

print("""
		Elija una opcion:
	1)Descargar la libreria (Automatico)
	2)Ya tengo instalada la libreria
	3)Salir
	""")

print("Tu opcion es.. ", end=" ")
deci = int(input())

if deci == 2:
	print("Excelente!! Vamos a continuar....")
	time.sleep(2)
	os.system("brain.py")




if deci == 1:
	print("Esta bien... El proceso comensara en breve.")
	os.system("instalador_pynput.bat")
	print("Este proceso puede demorar...")
	


if deci == 3:
	print("Esta bien, puedes volver cuando quieras!!!")
	input()
	
else:
	print("Comando desconocido vuelve a intentarlo")



	

	



