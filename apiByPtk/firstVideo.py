##### Suggested clean drone startup sequence #####
import time, sys
import ps_drone #Imports the PS-Drone-API
import cv2 

drone = ps_drone.Drone() #Initials the PS-Drone-API
drone.startup() #Connects to the drone and starts subprocesses
drone.reset()
while (drone.getBattery()[0]==-1): time.sleep(0.1) #Reset completed ?
print "Battery:"+str(drone.getBattery()[0])+"% "+str(drone.getBattery()[1])
drone.useDemoMode(True) #15 basic datasets per second
drone.getNDpackage(["demo","vision detect"]) #Packets to decoded
time.sleep(0.5) #Gives time to fully awake
##### Mainprogram #####
CDC = drone.ConfigDataCount
drone.setConfigAllID() #Go to multiconfiguration-mode
drone.sdVideo() #Choose lower resolution
drone.frontCam() #Choose front view
while CDC==drone.ConfigDataCount: time.sleep(0.001) #Wait until it is done
drone.startVideo() #Start video-function
drone.showVideo() #Display the video
print "<space> to toggle front- and groundcamera, 'z' key to stop"
IMC = drone.VideoImageCount #Number of encoded videoframes
stop = False
ground = False #To toggle front- and groundcamera

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
