def version():
	return 1.0

def crea_dir(directorio):
	if os.access(directorio,0):
		print "el directorio ya existe"
	else:
		os.mkdir(directorio)
	 	
