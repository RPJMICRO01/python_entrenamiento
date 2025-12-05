#!/usr/bin/python3

# funcion para cancelar el programa de manera ordenada

def signal_handler(key, frame):
	print("\n\n[*] Exiting...\n")
	sys.exit(1)

# mostrar informacion

print("R.G.\n17\nCH")
