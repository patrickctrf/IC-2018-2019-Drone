#########
# firstVideo.py
# This program is part of the online PS-Drone-API-tutorial on www.playsheep.de/drone.
# It shows the general usage of the video-function of a Parrot AR.Drone 2.0 using the PS-Drone-API.
# The drone will stay on the ground.
# Dependencies: a POSIX OS, openCV2, PS-Drone-API 2.0 beta or higher.
# (w) J. Philipp de Graaff, www.playsheep.de, 2014
##########
# LICENCE:
#   Artistic License 2.0 as seen on http://opensource.org/licenses/artistic-license-2.0 (retrieved December 2014)
#   Visit www.playsheep.de/drone or see the PS-Drone-API-documentation for an abstract from the Artistic License 2.0.
###########

##### Suggested clean drone startup sequence #####
import time, sys
sys.path.insert(0, 'lib')
import ps_drone                                             # Import PS-Drone

drone = ps_drone.Drone()                                     # Start using drone
drone.startup()                                              # Connects to drone and starts subprocesses

drone.reset()                                                # Sets drone's status to good (LEDs turn green when red)
while (drone.getBattery()[0] == -1):  time.sleep(0.1)    # Waits until drone has done its reset
print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1])	# Gives a battery-status
drone.useDemoMode(True)                                      # Just give me 15 basic dataset per second (is default anyway)

##### Mainprogram begin #####
config = None
print("BLALBLA")
for i in drone.ConfigData: print(i)

def setConfigPersistent(key, value):
    def getBitRate(drone):
        # drone.getConfig()
        for i in drone.ConfigData:
            if i[0] == key: #"video:video_codec":
                print(i)
                return int(i[1])

    print("Setting " + key + ", Pre: " + str(getBitRate(drone)))
    set = False
    while not set:
        drone.setConfigAllID()                                       # Go to multiconfiguration-mode
        # drone.sdVideo()                                              # Choose lower resolution (hdVideo() for...well, guess it)
        # drone.frontCam()                                             # Choose front view
        CDC = drone.ConfigDataCount
        print("-------------")
        drone.setMConfig(key, value)
        print("-------------")
        while CDC == drone.ConfigDataCount:       time.sleep(0.0001) # Wait until it is done (after resync is done)
        print("Retrying ")
        if int(getBitRate(drone)) == int(value): set = True

    print("!@@@")
    print("Post: " + str(getBitRate(drone)))

setConfigPersistent("video:video_channel", "1")
# setConfigPersistent("video:video_codec", "135")
# setConfigPersistent("video:bitrate_ctrl_mode", "2")
# setConfigPersistent("video:bitrate", "1000")
# setConfigPersistent("video:codec_fps", "20")
drone.fastVideo()
drone.startVideo()                                           # Start video-function
drone.showVideo()                                            # Display the video

##### And action !
print "Use <space> to toggle front- and groundcamera, any other key to stop"
IMC =    drone.VideoImageCount                               # Number of encoded videoframes
stop =   False
ground = False


while not stop:
    while drone.VideoImageCount == IMC: time.sleep(0.01)     # Wait until the next video-frame
    IMC = drone.VideoImageCount
    key = drone.getKey()                                     # Gets a pressed key
    if key==" ":
        if ground:              ground = False
        else:                   ground = True
        drone.groundVideo(ground)                            # Toggle between front- and groundcamera. Hint: options work for all videocommands
    elif key and key != " ":    stop =   True
