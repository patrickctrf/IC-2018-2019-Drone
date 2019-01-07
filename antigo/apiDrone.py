"""
Este código contém comandos em alto nível para controle das funcionalidade básicas do drone
A API original se encontra no arquivo ps_drone.py e o arquivo para teste da obtenção do vídeo frontal é firstVideo.py
"""

import ps_drone.py
import firstVideo.py

# Esta função serve para mover o drone em linha reta na dada direção.
# Os valores aceitáveis como parâmetro de speed variam em float de 0.0 a 1.0.
def moveFrente(speed):
	drone.setSpeed(speed)
	drone.moveFoward()

# Esta função serve para mover o drone em linha reta na dada direção.
# Os valores aceitáveis como parâmetro de speed variam em float de 0.0 a 1.0.
def moveTras(speed):
	drone.setSpeed(speed)
	drone.moveBackward()

# Esta função serve para mover o drone em linha reta na dada direção.
# Os valores aceitáveis como parâmetro de speed variam em float de 0.0 a 1.0.
def moveDireita(speed):
	drone.setSpeed(speed)
	drone.moveRight()

# Esta função serve para mover o drone em linha reta na dada direção.
# Os valores aceitáveis como parâmetro de speed variam em float de 0.0 a 1.0.
def moveEsquerda(speed):
	drone.setSpeed(speed)
	drone.moveLeft()

# Este comando faz o drone girar um valor em graus (positivo ou negativo)
def giraAngulo(ang):
	drone.turnAngle(ang,1)

#Esta função faz o drone parar de se mover
def parar():
	dorne.hover()

def desce():
	drone.moveDown()

def sobe():
	drone.moveUp()
	
def decola():
	drone.takeoff()
	
def pousa():
	drone.land()
	
def exibeVideoFrontal()
	while stop != True: #Roda ate mandar parar
	while drone.VideoImageCount==IMC: time.sleep(0.01) #Wait for next image
	IMC = drone.VideoImageCount #Number of encoded videoframes
	key = drone.getKey()
	
	video = drone.VideoImage
	print video.shape
	
	video = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
	cv2.imshow("Frame", video)
	cv2.waitKey(0)

	if key==" ":
		if ground: ground = False
		else: ground = True
		drone.groundVideo(ground) #Toggle between front- and groundcamera.
	elif key and key == "z": stop = True
	
# Esta chamada define o PWM em cada motor do drone, variando de 0 a 255.
def pwmMotores( frenteEquerda, frenteDireta, trasEsquerda, trasDireita)
	drone.thrust( frenteEquerda, frenteDireta, trasEsquerda, trasDireita)
	

"""
elif key == "0":	drone.hover()
elif key == "w":	drone.moveForward()
elif key == "s":	drone.moveBackward()
elif key == "a":	drone.moveLeft()
elif key == "d":	drone.moveRight()
elif key == "q":	drone.turnLeft()
elif key == "e":	drone.turnRight()
elif key == "7":	drone.turnAngle(-10,1)
elif key == "9":	drone.turnAngle( 10,1)
elif key == "4":	drone.turnAngle(-45,1)
elif key == "6":	drone.turnAngle( 45,1)
elif key == "1":	drone.turnAngle(-90,1)
elif key == "3":	drone.turnAngle( 90,1)
elif key == "8":	drone.moveUp()
elif key == "2":	drone.moveDown()
elif key == "*":	drone.doggyHop()
elif key == "+":	drone.doggyNod()
elif key == "-":	drone.doggyWag()
elif key == "z":	drone.land()
elif key == "p":	drone.takeoff()
"""
