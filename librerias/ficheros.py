import os

def version():
	return 1.0

def crea_dir(directorio):
	if os.access(directorio,0):
		print "el directorio ya existe"
	else:
		os.mkdir(directorio)

def entorno():
	for clave,valor in os.environ.iteritems():
		if clave=='USER' or clave=='PATH' or clave=='USER':
			print valor	

def gordos(directorio, size):
	for x in os.listdir(directorio):
		if os.path.isfile(x)==TRUE and os.path.getsize(x)>size: 
			print os.path.getsize(x)

def visualizar(fichero):
	if not os.access(fichero,0):
		print "ficheronoexiste"
		return false
	f=open(fichero,'r')
	while True:
		linea=f.readline()
		
	archivo=open(fichero,"r")
	print archivo.read()
	
