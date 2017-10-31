from os import system
import curses

def get_param(prompt_string):
	screen.clear()
	screen.addstr(2, 2, prompt_string)
	screen.refresh()
	input = screen.getstr(10, 10, 60)
	return input

def execute_cmd(cmd_string):
	system("cls")
	a = system(cmd_string)
	print ""
	if a == 0:
		print "Operacion Completada Correctamente"
	else:
		print "Operacion Terminada con Errores"
	raw_input("Presiona Enter")
	print ""

x = 0
while x != ord('4'):
	screen = curses.initscr()
	screen.clear()
	screen.addstr(2, 2, "MYAUTOBACKUPS")
	screen.addstr(4, 2, "Selecciona una Opcion...")
	screen.addstr(6, 4, "1 - Configuracion de Inicio")
	screen.addstr(7, 4, "2 - Respaldo Local")
	screen.addstr(8, 4, "3 - Respaldo Nube")
	screen.addstr(9, 4, "4 - Salir")
	screen.addstr(10, 4, "")
	screen.refresh()
	x = screen.getch()
	if x == ord('1'):
		usern = get_param("Usuario de MySQL")
		passw = get_param("Contrasena de MySQL")
		db = get_param("Base de Datos")
		ruta = get_param("Ruta Local de Almacenamiento")
		with open('configuracion', 'a') as the_file:
			the_file.write(usern + '\n')
			the_file.write(passw + '\n')
			the_file.write(db + '\n')
			the_file.write(ruta)
		curses.endwin()
		execute_cmd("")
	if x == ord('2'):
		#with open('configuracion', 'r') as the_file:
		#	usernln = the_file.read()
		#	passwln = the_file.read()
		#	dbln = the_file.read()
		#	rutaln = the_file.read()
		#	usern = usernln.replace("\n","")
		#	passw = passwln.replace("\n","")
		#	db = dbln.replace("\n","")
		#	ruta = rutaln.replace("\n","")
		curses.endwin()
		execute_cmd("mysqldump -u " + usern + " --password=" + passw + " " + db + " > " + ruta + db + ".sql")
	if x == ord('3'):
		screen.addstr("Para la configuracion de respaldos en la nube instalar el cliente de google drive y en la carpeta de sincronizacion seleccionar la de backups")
		curses.endwin()
curses.endwin()