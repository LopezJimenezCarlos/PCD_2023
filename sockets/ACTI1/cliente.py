import threading
import sys
import socket
import pickle
import os

class Cliente():

	def __init__(self, host=input("Intoduzca la IP del servidor ?  "), port=int(input("Intoduzca el PUERTO del servidor ?  ")),nickname=(input("Intoduzca su nombre:  "))):#pido la ip, el puerto y el nickname por pantalla
		with open("Nicknames.txt",'a') as n: #hago un fichero donde guarde los usuarios
			n.write(nickname) #escribo el nickname pedido por pantalla
			n.write(" , ")#espacio para que quede mejor visualmente
		self.s = socket.socket()
		self.s.connect((host, int(port)))
		print('\n\tProceso con PID = ',os.getpid(), '\n\tHilo PRINCIPAL con ID =',threading.currentThread().getName(), '\n\tHilo en modo DAEMON = ', threading.currentThread().isDaemon(),'\n\tTotal Hilos activos en este punto del programa =', threading.active_count())
		threading.Thread(target=self.recibir, daemon=True).start()
	
		print('\nEscriba texto ?   ** Enviar = ENTER   ** Salir Chat = 1\n')
		
		while True:
				m=open
				msg = input(nickname)#le pongo al lado del input, el nickname, para que aparezca al escribir lo que quiera el usuario
				with open("u22166883AI1.txt",'a') as w:#fichero para meter los mensajes
					w.write(nickname)#aqui pongo para que salga de que usuario es el mensaje
					w.write(":")#para la estetica del fichero
					w.write(msg) #le paso el mensaje al fichero
					w.write(" , ")# para el formato del fichero, que quede mejor
				if msg != '1' : self.enviar(msg)
				else:
					print(" **** Me piro vampiro; cierro socket y mato al CLIENTE con PID = ", os.getpid())
					self.s.close()
					sys.exit()

	def recibir(self):
		print('\nHilo RECIBIR con ID =',threading.currentThread().getName(), '\n\tPertenece al PROCESO con PID', os.getpid(), "\n\tHilos activos TOTALES ", threading.active_count())
		while True:
			try:
				data = self.s.recv(32)
				if data: print(pickle.loads(data))
			except: pass

	def enviar(self, msg):
		self.s.send(pickle.dumps(msg))

arrancar = Cliente()
# Revisión parte del cliente  finalizada

		