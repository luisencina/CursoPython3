import sys

if(len(sys.argv) == 3):
	text = sys.argv[1]
	repeticiones = int(sys.argv[2]) 

	for r in range(repeticiones):
		print(text)
else:
	print("error, introduce los argurmentos correctamente")
	print("Ejemplo: escribi_lineas.py 'texto' 5")